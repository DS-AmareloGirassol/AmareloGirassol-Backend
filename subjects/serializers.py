from rest_framework import serializers
from . import models

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Subject
        fields = ['url', 'id', 'name', 'code']