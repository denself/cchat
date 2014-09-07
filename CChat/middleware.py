# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from model import User, AnonymousUser
__author__ = 'D.Ivanets'

SESSION_KEY = '_auth_user_id'


class SQLAlchemySessionMiddleware(object):
    def process_request(self, request):
        request.db_session = settings.SESSION()

    def process_response(self, request, response):
        try:
            session = request.db_session
        except AttributeError:
            return response
        try:
            session.commit()
            return response
        except:
            session.rollback()
            raise

    def process_exception(self, request, exception):
        try:
            session = request.db_session
        except AttributeError:
            return
        session.rollback()


def get_user(request):
    if SESSION_KEY in request.session:
        return request.db_session.query(User).filter_by(id=request.session[SESSION_KEY]).one()
    else:
        return AnonymousUser()


class SQLAlchemyAuthMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), \
            "The SQLAlchemy authentication middleware requires session middleware to be installed. Edit your " \
            "MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."

        request.user = SimpleLazyObject(lambda: get_user(request))