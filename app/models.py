from typing import Any
from django.db import models
from django.utils import timezone

# Create your models here.
class MeterPoint(models.Model):
    mpan = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.mpan

class Meter(models.Model):
    serial_number = models.CharField(max_length=50)
    meter_point = models.ForeignKey(MeterPoint, on_delete=models.CASCADE)
    def __str__(self):
        return self.serial_number

class Reading(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_date =models.DateTimeField(default=timezone.now)
    updated_date  = models.DateTimeField()
    name =  models.CharField(max_length=100)
    owner =  models.CharField(max_length=10)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    data_flow_file = models.CharField(max_length=20)

    def __str__(self):
        return self.name
