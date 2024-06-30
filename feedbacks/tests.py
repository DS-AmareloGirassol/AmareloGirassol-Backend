from django.test import TestCase

# Create your tests here.
from rest_framework import viewsets

from feedbacks import models
from feedbacks import serializers

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = models.Feedback.objects.all()
    serializer_class = serializers.FeedbackSerializer