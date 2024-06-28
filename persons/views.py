from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer
from subjects.serializers import SubjectSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()
    
    @action(detail=True, methods=['post'], url_path='add-subject')
    def add_subjects(self, request: Request, pk=None):
        user: Person = self.get_object()

        data = request.data

        try:
            user.add_all_subject_studied(data)
        except Exception as e:
            return Response({'errors': e.args}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Disciplinas cadastradas ao aluno com sucesso'}, status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'], url_path='subject')
    def subjects(self, request: Request, pk=None):
        user: Person = self.get_object()

        try:
            subjects_list = user.get_all_subjects()
            serializer = SubjectSerializer(subjects_list, many=True, context={'request': request})
        except Exception as e:
            return Response({'errors': e.args}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)