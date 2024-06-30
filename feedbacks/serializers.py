from rest_framework import serializers

from . import models

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Feedback
        fields = ['url', 'id', 'metodologia', 'didatica', 'suporte_professor', 
                  'monitoria', 'indice_recomendacao', 'user', 'subject']