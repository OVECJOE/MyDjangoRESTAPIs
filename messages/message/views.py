'''The module containing the views of this API'''
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import MessageSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Message
from rest_framework import status


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class MessageViewSet(APIView):
    '''The viewset for a message instance'''
    queryset = Message.objects.all()

    def post(self, request, format=None):
        '''post request'''
        data = {
            'message': request.data.get('message'),
            'user': request.user.pk
        }

        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            data = serializer.data.copy()
            del data['user']
            data['created_by'] = UserSerializer(request.user).data

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthTokenLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.pk,
            'username': user.username,
            'email': user.email,
            'token': token.key,
        })
