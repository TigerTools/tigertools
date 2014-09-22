from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group

class UserListingField(serializers.RelatedField):
    def to_native(self, value):
        return ('%s') % (value.username)

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    user = UserListingField()
    class Meta:
        model = Token
        depth = 1
        fields = ('key', 'user')

