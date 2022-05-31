from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageViewSet.as_view()),
]
