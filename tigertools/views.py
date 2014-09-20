from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.db.models import Q
from rest_framework import viewsets, views
from rest_framework.response import Response
from gas.models import GasLineItem, GasPurchase, GasStation
from django.contrib.auth.models import User, Group
from tigertools.serializers import GasLineItemSerializer, GasPurchaseSerializer, GasStationSerializer
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
import pprint


class TigerToolsKeyConstructor(KeyConstructor):
    unique_view_id = bits.UniqueViewIdKeyBit()
    language = bits.LanguageKeyBit()
    format = bits.FormatKeyBit()

class TigerToolsRetrieveKeyConstructor(TigerToolsKeyConstructor):
    retrieve_sql_query = bits.RetrieveSqlQueryKeyBit()

class TigerToolsListKeyConstructor(TigerToolsKeyConstructor):
    list_sql_query = bits.ListSqlQueryKeyBit()

def list_key_constructor():
    return TigerToolsListKeyConstructor(memoize_for_request=True)
def retrieve_key_constructor():
    return TigerToolsRetrieveKeyConstructor(memoize_for_request=True)

# Create your views here.
def index(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response('tigertools/index.html',
                             context_instance=context)

class TigerToolsViewSet(DetailSerializerMixin, viewsets.ModelViewSet):
    class Meta:
        abstract = True
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup = self.kwargs.get(lookup_url_kwarg, None)
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        slug = self.kwargs.get(self.slug_url_kwarg, None)

        if lookup is not None:
            filter_kwargs = {self.lookup_field: lookup}
        elif pk is not None and self.lookup_field == 'pk':
            warnings.warn(
                PendingDeprecationWarning
            )
            filter_kwargs = {'pk': pk}
        elif slug is not None and self.lookup_field == 'pk':
            warnings.warn(
                PendingDeprecationWarning
            )
            filter_kwargs = {self.slug_field: slug}
        else:
            raise ImproperlyConfigured(
                (self.__class__.__name__, self.lookup_field)
            )

        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

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

