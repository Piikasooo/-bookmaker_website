from django.urls import path
from .views import register, test


app_name = "user"

urlpatterns = [
    path('register/', register, name='register'),
    path('test/', test, name='test'),
]