# pylint: disable=abstract-method
'''A module containing the serializers for this API'''
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class UserSerializer(serializers.ModelSerializer):
    '''A serializer class for the User model'''
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['groups', 'user_permissions']
        extra_kwargs = {'password': {'write_only': True}}


class MessageSerializer(serializers.ModelSerializer):
    '''A serializer class for the Message model'''
    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        '''Creates a user'''
        message = validated_data.get('message')
        user = validated_data.get('user')

        message = Message.objects.create(
            message=message,
            user=user
        )
        print(type(message))
        return message
