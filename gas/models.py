from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from tigertools.models import Ledger, LineItem, Location, Purchase, Vehicle

class GasStation(Location):
    def __unicode__( self ):
        return ("%s - %s" % (self.name, self.address))
    name = models.CharField(max_length = 128, default="unknown")

class GasVehicle(Vehicle):
    def __unicode__( self ):
        return ("%s, %s %s" % (self.year, self.make, self.name))

class GasPurchase(Purchase):
    def __unicode__( self ):
        return ("%s @ %s" % (self.gallons, self.gas_station))
    gallons = models.FloatField('Total Gallons', default=0)
    milage = models.IntegerField('Milage on Odometer', default=0)
    gas_station = models.ForeignKey(GasStation)

class GasLineItem(LineItem):
    gas_vehicle = models.ForeignKey(GasVehicle)
    gas_purchase = models.OneToOneField(GasPurchase)

