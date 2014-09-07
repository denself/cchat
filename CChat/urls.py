from django.conf.urls import patterns, include, url
from django.conf import settings
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CChat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^auth/', include('auth.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))