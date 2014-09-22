from rest_framework import serializers
from gas.models import GasLineItem, GasPurchase, GasStation, GasVehicle

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

class GasVehicleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasVehicle
        depth = 1
        fields = ('url', 'user', 'name', 'make', 'year')