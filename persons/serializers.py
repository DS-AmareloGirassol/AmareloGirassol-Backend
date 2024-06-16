from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, ModelSerializer
from rest_framework import serializers

from .models import Person


class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'url', 'name', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

class AuthenticationGetTokenParamsSerializer(Serializer):
    token = serializers.ReadOnlyField()