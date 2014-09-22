import models
from django import forms
from django.contrib import admin

# Register your models here.

class HashAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.Hash, HashAdmin)
