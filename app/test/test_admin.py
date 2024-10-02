from django.test import TestCase
from app.models import MeterPoint, Meter, Reading
from django.contrib.admin.sites import AdminSite
from app.admin import ReadingAdmin

class AdminTests(TestCase):
    def setUp(self):
        self.meter_point = MeterPoint.objects.create(mpan="1234567890123")
        self.meter = Meter.objects.create(meter_point=self.meter_point, serial_number="ABC123")
        self.reading = Reading.objects.create(
            meter=self.meter,
            value=100.5,
            date="2023-01-01",
            flow_file="test_file.txt"
        )
        self.site = AdminSite()

    def test_reading_admin_search(self):
        reading_admin = ReadingAdmin(Reading, self.site)
        
        # Test search by MPAN
        queryset = reading_admin.get_search_results(None, Reading.objects.all(), "1234567890123")[0]
        self.assertIn(self.reading, queryset)

        # Test search by meter serial number
        queryset = reading_admin.get_search_results(None, Reading.objects.all(), "ABC123")[0]
        self.assertIn(self.reading, queryset)

        # Test search by non-existent value
        queryset = reading_admin.get_search_results(None, Reading.objects.all(), "NonExistent")[0]
        self.assertNotIn(self.reading, queryset)

    def test_reading_admin_list_display(self):
        reading_admin = ReadingAdmin(Reading, self.site)
        self.assertIn('meter', reading_admin.list_display)
        self.assertIn('value', reading_admin.list_display)
        self.assertIn('date', reading_admin.list_display)
        self.assertIn('flow_file', reading_admin.list_display)