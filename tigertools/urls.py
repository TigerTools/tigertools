from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework import routers 
import autocomplete_light
import gas


# import every app/autocomplete_light_registry.py
autocomplete_light.autodiscover()
admin.autodiscover()
template_name = {'template_name': 'rest_framework/login.html'}
router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register(r'gas/lineitems', gas.views.GasLineItemViewSet)
router.register(r'gas/purchases', gas.views.GasPurchaseViewSet)
router.register(r'gas/stations', gas.views.GasStationViewSet)
router.register(r'gas/vehicles', gas.views.GasVehicleViewSet)

urlpatterns = patterns('',
    url(r'^gas/', include(gas.urls, namespace='gas')),
    url(r'^', include(router.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^login/$', 'django.contrib.auth.views.login', template_name, name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
