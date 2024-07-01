from rest_framework import serializers

from . import models
from persons.models import Person
from subjects.models import Subject

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    class Meta:
        model = models.Feedback
        fields = ['url', 'id', 'metodologia', 'trabalho', 'provas', 
                  'material', 'facilidade', 'user', 'subject']