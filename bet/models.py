from django.db import models
from user.models import User


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class BetStatus(models.Model):

    class Status(models.IntegerChoices):
        in_processing = 1
        approved = 2
        failure = 3
        in_archive = 4
    status = models.IntegerField(choices=Status.choices)


class EventResult(models.Model):
    name = models.CharField(max_length=1000)
    result = models.IntegerField()


class Event(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateTimeField()
    event_result = models.ForeignKey(EventResult, on_delete=models.DO_NOTHING)


class EventStatus(models.Model):
    name = models.CharField(max_length=1000)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)


class EventGroup(models.Model):
    name = models.CharField(max_length=1000)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)


class KindOfSport(models.Model):
    name = models.CharField(max_length=1000)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
