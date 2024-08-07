from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.
class MeterPoint(models.Model):
    mpan = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.mpan

class Meter(models.Model):
    meter_point = models.ForeignKey(MeterPoint, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.serial_number

class Reading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateField()
    filename = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.meter.serial_number} - {self.value} on {self.date}"