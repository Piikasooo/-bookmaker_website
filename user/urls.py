from django.urls import path
from .views import user_registration


app_name = "user"

urlpatterns = [
    path('registration', user_registration, name='registration'),
]