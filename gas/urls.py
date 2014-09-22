from django.conf.urls import patterns, include, url
from rest_framework import routers 
from gas import views

# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'rest_framework/gaslogin.html'}, name='login'),
)

