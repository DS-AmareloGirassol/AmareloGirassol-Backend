from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, ModelSerializer
from rest_framework import serializers

from .models import Person


class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'url', 'name', 'email', 'description', 
                  'semester_being_attended', 'current_fluxo_position', 'expected_fluxo_position']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

class AuthenticationGetTokenParamsSerializer(Serializer):
    token = serializers.ReadOnlyField()