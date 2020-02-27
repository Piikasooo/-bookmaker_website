from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    birthday = models.DateField("Birthday")
    money = models.DecimalField(max_digits=100000, decimal_places=2)
