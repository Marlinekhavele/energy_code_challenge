from django.test import TestCase
from decimal import Decimal
from .models import MeterPoint, Meter, Reading

class MeterReadingsTestCase(TestCase):
    def setUp(self):
        self.meter_point = MeterPoint.objects.create(mpan="1234567890")
        self.meter = Meter.objects.create(meter_point=self.meter_point, serial_number="SN123")
        Reading.objects.create(meter=self.meter, value=Decimal('100.123'), date="2024-01-01", filename="sample.txt")

    def test_reading_creation(self):
        reading = Reading.objects.get(meter=self.meter)
        self.assertEqual(reading.value, Decimal('100.123'))
