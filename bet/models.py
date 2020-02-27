from django.db import models
from user.models import User


class BetCategories(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    uuid = models.CharField(max_length=36, unique=True)


class Game(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    category = models.ForeignKey(BetCategories, on_delete=models.CASCADE)


class Bets(models.Model):
    game = models.ManyToManyField(Game)
    condition = models.CharField(max_length=3000)
    first_coefficient = models.DecimalField(max_digits=2, decimal_places=2)
    second_coefficient = models.DecimalField(max_digits=2, decimal_places=2)
    third_coefficient = models.DecimalField(max_digits=2, decimal_places=2)


class UserBets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    bet = models.ManyToManyField(Bets)
    how_much_bet_user = models.DecimalField(max_digits=6, decimal_places=2)
    bet_date = models.DateTimeField()
