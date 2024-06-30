
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.user.authentication import create_token_response, create_valid_token_response

from . import serializers


class Authentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            
            user = serializer.validated_data['user']

            token = None
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                pass

            token = token if token else Token.objects.create(user=user)
        except Exception as error:
            return Response({'detail': f'Unable to log in with provided credentials: {str(error)}'}, status.HTTP_401_UNAUTHORIZED)

        try:
            response = Authentication._create_and_update_login_response(token.key, user.id, user.email, user.name)

            return Response(response)
        except Exception as error:
            return Response({'authentication error': f'{str(error)}'}, status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        params_serializer = serializers.AuthenticationGetTokenParamsSerializer(data=request.data)
        if not params_serializer.is_valid():
            return Response(params_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            Token.objects.get(pk=request.data['token'])

            is_valid_token = True
        except ObjectDoesNotExist:
            is_valid_token = False

        response = create_valid_token_response(is_valid_token)

        return Response(response)

    def _create_and_update_login_response(token, user_id, user_email, user_name):
        response = create_token_response(token, user_id, user_email, user_name)

        return response
    
class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()

            return Response({"detail": "Logout successful"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": f"Failed to logout: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)