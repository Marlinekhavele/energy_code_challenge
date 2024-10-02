from django.db import models

# Create your models here.
class MeterPoint(models.Model):
    mpan = models.CharField(max_length=21, unique=True)

    def __str__(self):
        return self.mpan

class Meter(models.Model):
    meter_point = models.ForeignKey(MeterPoint, on_delete=models.CASCADE, related_name='meters')
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.serial_number} ({self.meter_point.mpan})"

class Reading(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='readings')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    flow_file = models.CharField(max_length=255)

    class Meta:
        unique_together = ('meter', 'date')

    def __str__(self):
        return f"{self.meter.serial_number} - {self.date}: {self.value:.2f}"