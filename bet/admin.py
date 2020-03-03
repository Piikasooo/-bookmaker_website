from django.contrib import admin
from .models import BetCategories, Game, Coefficients, Bets, UserBets

admin.site.register(BetCategories)
admin.site.register(Game)
admin.site.register(Coefficients)
admin.site.register(Bets)
admin.site.register(UserBets)
