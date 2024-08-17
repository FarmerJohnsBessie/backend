from django.urls import path
from api import views

urlpatterns = [
    path('chat/', views.chat_with_bot),
]