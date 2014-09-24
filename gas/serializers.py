from rest_framework import serializers
from gas.models import GasLineItem, GasPurchase, GasStation, GasVehicle

class GasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        abstract = True
    def save(self, user, **kwargs):
        self._data = None
        if isinstance(self.object, list):
            [self.save_object(item, **kwargs) for item in self.object]

            if self.object._deleted:
                [self.delete_object(item) for item in self.object._deleted]
        else:
            self.object.user = user
            self.save_object(self.object, **kwargs)

class GasLineItemSerializer(GasSerializer):
    user = serializers.PrimaryKeyRelatedField()
    gas_purchase = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasLineItem
        depth = 1
        fields = ('url', 'gas_purchase', 'user', 'amount', 'type', 'created', 'updated')

class GasPurchaseSerializer(GasSerializer):
    user = serializers.PrimaryKeyRelatedField()
    gas_station = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasPurchase
        depth = 1
        fields = ('url', 'gas_station', 'user', 'gallons', 'milage', 'tax')

class GasStationSerializer(GasSerializer):
    user = serializers.PrimaryKeyRelatedField()
    class Meta:
        model = GasStation
        depth = 1
        fields = ('url', 'user', 'address', 'latitude', 'longitude')

class GasVehicleSerializer(GasSerializer):
    class Meta:
        model = GasVehicle
        depth = 1
        fields = ('url', 'name', 'make', 'year')
