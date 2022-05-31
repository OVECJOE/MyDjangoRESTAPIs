'''A module that contains the message model'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4


class Message(models.Model):
    '''A model representing a message'''
    id = models.UUIDField(primary_key=True, default=uuid4)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(verbose_name='Created At', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated At', default=timezone.now)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='created_by')

    def __str__(self):
        '''String representation of a Message instance'''
        return f'{self.message}'
