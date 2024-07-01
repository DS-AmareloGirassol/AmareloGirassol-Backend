from rest_framework import serializers

from . import models
from persons.models import Person

class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())

    class Meta:
        model = models.Post
        fields = ['url', 'id', 'title', 'description', 'user', 'user_name', 'link']