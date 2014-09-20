from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from fields import CurrencyField

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

def compose_ledger(obj, collection):
    count=0
    for item in collection:
        count += 1
        obj.amount += item.amount
    obj.average = (obj.amount/count) if count > 1 else obj.amount
    return obj

class Location(models.Model):
    def __unicode__( self ):
        return ("%s" % (self.address))
    class Meta:
        abstract = True
    user = models.ForeignKey(User)
    address =models.CharField(max_length = 200, blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

class Purchase(models.Model):
    def __unicode__( self ):
        return ("%s" % (self.amount))
    class Meta:
        abstract = True
    user = models.ForeignKey(User)
    tax = CurrencyField('tax', default=0)

class Ledger(models.Model):
    def __unicode__( self ):
        return ("%s" % (self.amount))
    class Meta:
        abstract = True
    amount = CurrencyField('amount', default=0)
    average = 0

class LineItem(Ledger):
    
    TYPE_CREDIT = 'credit'
    TYPE_DEDUCTION = 'deduction'

    Types = (
        (TYPE_CREDIT, 'Credit'),
        (TYPE_DEDUCTION, 'Deduction'),
    )

    def __unicode__( self ):
        return ("%s" % (self.amount))
    class Meta:
        abstract = True
    user = models.ForeignKey(User)
    type = models.CharField(max_length=10, choices=Types, default=TYPE_CREDIT)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

