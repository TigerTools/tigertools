from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.db.models import Q
from rest_framework import viewsets, views
from rest_framework.response import Response
from gas.models import GasLineItem, GasPurchase, GasStation, GasVehicle
from tigertools.views import (
    TigerToolsKeyConstructor, 
    TigerToolsRetrieveKeyConstructor, 
    TigerToolsKeyConstructor,  
    TigerToolsListKeyConstructor, 
    TigerToolsRetrieveKeyConstructor,
    TigerToolsViewSet,
    list_key_constructor,
    retrieve_key_constructor
)

from gas.serializers import (
    GasLineItemSerializer, 
    GasPurchaseSerializer, 
    GasStationSerializer, 
    GasVehicleSerializer
)

from django.shortcuts import get_object_or_404
from rest_framework_extensions.mixins import DetailSerializerMixin
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.etag.mixins import ETAGMixin 
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.etag.decorators import etag
from rest_framework_extensions.key_constructor.constructors import (
    KeyConstructor
)
from rest_framework_extensions.key_constructor import bits
import operator

class GasLineItemViewSet(TigerToolsViewSet):
    queryset = GasLineItem.objects.all()
    serializer_class = GasLineItemSerializer
    serializer_detail_class = GasLineItemSerializer
    def get_queryset(self):
        return GasLineItem.objects.filter(user=self.request.user)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(retrieve_key_constructor())
    def retrieve(self, request, *args, **kwargs):
        return super(GasLineItemViewSet, self).retrieve(request, *args, **kwargs)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(list_key_constructor())
    def list(self, request, *args, **kwargs):
        return super(GasLineItemViewSet, self).list(request, *args, **kwargs)

class GasPurchaseViewSet(TigerToolsViewSet):
    queryset = GasPurchase.objects.all()
    serializer_class = GasPurchaseSerializer
    serializer_detail_class = GasPurchaseSerializer
    def get_queryset(self):
        return GasPurchase.objects.filter(user=self.request.user)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(retrieve_key_constructor())
    def retrieve(self, request, *args, **kwargs):
        return super(GasPurchaseViewSet, self).retrieve(request, *args, **kwargs)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(list_key_constructor())
    def list(self, request, *args, **kwargs):
        return super(GasPurchaseViewSet, self).list(request, *args, **kwargs)

class GasStationViewSet(TigerToolsViewSet):
    queryset = GasStation.objects.all()
    serializer_class = GasStationSerializer
    serializer_detail_class = GasStationSerializer
    def get_queryset(self):
        return GasStation.objects.filter(user=self.request.user)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(retrieve_key_constructor())
    def retrieve(self, request, *args, **kwargs):
        return super(GasStationViewSet, self).retrieve(request, *args, **kwargs)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(list_key_constructor())
    def list(self, request, *args, **kwargs):
        return super(GasStationViewSet, self).list(request, *args, **kwargs)

class GasVehicleViewSet(TigerToolsViewSet):
    queryset = GasVehicle.objects.all()
    serializer_class = GasVehicleSerializer
    serializer_detail_class = GasVehicleSerializer
    def get_queryset(self):
        return GasVehicle.objects.filter(user=self.request.user)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(retrieve_key_constructor())
    def retrieve(self, request, *args, **kwargs):
        return super(GasVehicleViewSet, self).retrieve(request, *args, **kwargs)
    
    @cache_control(must_revalidate=True,max_age=10)
    @etag(list_key_constructor())
    def list(self, request, *args, **kwargs):
        return super(GasVehicleViewSet, self).list(request, *args, **kwargs)

