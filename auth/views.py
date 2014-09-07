# import json
from django.contrib import auth
# from django.http import HttpResponse
from django.core import mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
import re
from sqlalchemy.orm.exc import NoResultFound
from model import User, EmailConfirmation


def login(request):
    errors = []
    if request.POST:
        email = request.POST.get('auth_email', '')
        try:
            validate_email(email)
        except ValidationError:
            errors.append({'field': 'Email', 'message': 'Invalid email'})
        password = request.POST.get('auth_password', '')
        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            errors.append({'field': 'Email', 'message': 'Incorrect credentials'})
    return render_to_response('auth/login.html',
                              {'errors': errors},
                              context_instance=RequestContext(request))


def signup(request):
    errors = []
    if request.POST:
        email = request.POST.get('auth_email', '')
        password1 = request.POST.get('auth_password', '')
        password2 = request.POST.get('auth_conf_password', '')
        try:
            validate_email(email)
        except ValidationError:
            errors.append({'field': 'Email', 'message': 'Invalid email'})
        if len(password1) < 8:
            errors.append({'field': 'Password', 'message': "Password must be 8 symbols or longer"})
        elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password1):
            errors.append({'field': 'Password', 'message': "Password must contain upper or lower case letters,"
                                                           " numbers or symbols @#$%^&+="})
        if password1 != password2:
            errors.append({'field': 'Password', 'message': "Passwords doesn't match"})
        if not errors:
            user = User(email, password1)
            conf = EmailConfirmation(user)
            request.db_session.add_all([user, conf])
            link = 'http://%s/auth/email_conf/%s/' % (request.META['HTTP_HOST'], conf.hash)
            mail.send_mail('Account registration',
                           'Welcome to %s \n'
                           'Your registration information: \n'
                           'Email: %s\n'
                           'Password: %s\n'
                           'Please, follow this link to confirm your email:'
                           '%s' % (request.META['HTTP_HOST'], email, password1, link),
                           'admin@localhost',
                           [email],
                           fail_silently=False)
            request.db_session.commit()
            return render_to_response('auth/signup_ok.html',
                                      {'errors': errors},
                                      context_instance=RequestContext(request))
    return render_to_response('auth/signup.html',
                              {'errors': errors},
                              context_instance=RequestContext(request))


def email_conf(request, hash_code):
    try:
        ec = request.db_session.query(EmailConfirmation)\
            .filter_by(hash=hash_code)\
            .filter(EmailConfirmation.dt_use == None).one()
    except NoResultFound:
        raise Http404
    if ec.dt_use:
        raise Http404
    ec.use()
    return render_to_response('auth/email_ok.html',
                              context_instance=RequestContext(request))