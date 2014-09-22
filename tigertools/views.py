from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.db.models import Q
from rest_framework import viewsets, views
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
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

