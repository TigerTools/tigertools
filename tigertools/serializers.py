from rest_framework import serializers
from gas.models import GasLineItem, GasPurchase, GasStation
from django.contrib.auth.models import User, Group

class GasLineItemSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    gas_purchase = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasLineItem
        depth = 1
        fields = ('url', 'gas_purchase', 'user', 'amount', 'type', 'created', 'updated')

class GasPurchaseSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    gas_station = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasPurchase
        depth = 1
        fields = ('url', 'gas_station', 'user', 'gallons', 'milage', 'tax')

class GasStationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasStation
        depth = 1
        fields = ('url', 'user', 'address', 'latitude', 'longitude')
