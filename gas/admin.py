import models
import autocomplete_light
from django import forms
from django.contrib import admin

# Register your models here.

class GasLineItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.GasLineItem, GasLineItemAdmin)

class GasPurchaseAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.GasPurchase, GasPurchaseAdmin)

class GasStationAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.GasStation, GasStationAdmin)
