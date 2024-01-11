import datetime
import django.utils.timezone

from django.db import models
from django.utils.timezone import now


# Create your models here.
class Mission(models.Model):
    location = models.CharField("where is the emergency", max_length=100)
    date = models.DateField("when the emergency was issued")
    duration = models.DurationField("time needed to resolve the emergency")


class Vehicle(models.Model):
    common_name = models.CharField("slang name", max_length=50)
    vehicle_index = models.CharField("coded Name", max_length=50)
    max_crew = models.IntegerField("max # crew")
    tot_km = models.IntegerField("total KM for vehicle")
    in_operation = models.ForeignKey(Mission,
                                     on_delete=models.SET_NULL,
                                     null=True)
    # questa è la paarte 1:N della relazione con  mission


class Crew(models.Model):
    service_veichle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    issued = models.DateField()
    foreman = models.IntegerField()


class CrewMate(models.Model):
    name = models.CharField()
    rank = models.CharField()
    crew_id = models.ForeignKey(Crew, on_delete=models.SET_NULL, null=True)
