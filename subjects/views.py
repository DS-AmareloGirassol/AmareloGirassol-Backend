from rest_framework import viewsets

from subjects import models
from subjects import serializers

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer