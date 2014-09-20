from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.contrib import admin
import autocomplete_light
from rest_framework import routers 
from tigertools import views
# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'gaslineitems', views.GasLineItemViewSet)
router.register(r'gaspurchases', views.GasPurchaseViewSet)
router.register(r'gasstations', views.GasStationViewSet)

template_name = {'template_name': 'rest_framework/login.html'}

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^gas/login/$', 'django.contrib.auth.views.login', {'template_name': 'rest_framework/gaslogin.html'}, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login', template_name, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
