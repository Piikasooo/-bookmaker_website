from django.db import models
from user.models import User


class BetCategories(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    uuid = models.CharField(max_length=36, unique=True)


class Game(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    category = models.ForeignKey(BetCategories, on_delete=models.CASCADE)


class Coefficients(models.Model):
    coefficient = models.DecimalField(max_digits=2, decimal_places=2)
    coeff_start_date = models.DateTimeField(auto_now_add=True)
    coeff_until_date = models.DateTimeField(blank=True, null=True)


class Bets(models.Model):
    game = models.ManyToManyField(Game)
    condition = models.CharField(max_length=3000)
    choice = models.ForeignKey(Coefficients, on_delete=models.DO_NOTHING)


class UserBets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    bet = models.ForeignKey(Bets, on_delete=models.CASCADE, default=None)
    user_bet_money = models.DecimalField(max_digits=6, decimal_places=2)
    bet_date = models.DateTimeField(auto_now_add=True)