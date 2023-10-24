from django.db import models
from django.utils import timezone
import datetime


INT_FOR_FOUND_HOURS = 3600
INT_FOR_FOUND_MINUTES = 60


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    time_of_entering = visit.entered_at
    time_of_leaving = visit.leaved_at
    if time_of_leaving:
        delta = timezone.localtime(value=time_of_leaving) - timezone.localtime(value=time_of_entering)
    else:
        delta = timezone.localtime() - timezone.localtime(value=time_of_entering)
    seconds = delta.total_seconds()
    return seconds


def format_duration(visit):
    hours = get_duration(visit) // INT_FOR_FOUND_HOURS
    minutes = (get_duration(visit) % INT_FOR_FOUND_HOURS) // INT_FOR_FOUND_MINUTES
    delta = '{}ч {}мин'.format(int(hours), int(minutes))
    return delta


def is_visit_long(visit, minutes=60):
    duration_in_min = get_duration(visit) // INT_FOR_FOUND_MINUTES
    return duration_in_min >= minutes
