from django.test import TestCase
from app.models import MeterPoint, Meter, Reading
from django.db.utils import IntegrityError



class ModelTests(TestCase):
    def setUp(self):
        self.meter_point = MeterPoint.objects.create(mpan="1234567890123")
        self.meter = Meter.objects.create(meter_point=self.meter_point, serial_number="ABC123")

    def test_meter_point_creation(self):
        self.assertEqual(str(self.meter_point), "1234567890123")

    def test_meter_creation(self):
        self.assertEqual(str(self.meter), "ABC123 (1234567890123)")

    def test_reading_creation(self):
        reading = Reading.objects.create(
            meter=self.meter,
            value=100.5,
            date="2023-01-01",
            flow_file="test_file.txt"
        )
        self.assertEqual(str(reading), "ABC123 - 2023-01-01: 100.50")

    def test_unique_constraints(self):
        Reading.objects.create(
            meter=self.meter,
            value=100.5,
            date="2023-01-01",
            flow_file="test_file.txt"
        )
        with self.assertRaises(IntegrityError):
            Reading.objects.create(
                meter=self.meter,
                value=200.5,
                date="2023-01-01",
                flow_file="test_file2.txt"
            )