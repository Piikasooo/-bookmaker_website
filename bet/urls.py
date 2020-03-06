from django.urls import path
from .views import get_all


app_name = "bet"

urlpatterns = [
    path('all/', get_all, name='get_all')
]