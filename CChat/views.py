from django.http import Http404, HttpResponse

__author__ = 'D.Ivanets'
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return HttpResponse(request.user.email)


