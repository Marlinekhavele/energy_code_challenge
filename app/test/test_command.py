
from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from app.models import MeterPoint, Meter, Reading
from django.core.exceptions import ValidationError
from unittest.mock import patch
import tempfile
import os

class ImportCommandTests(TestCase):
    def setUp(self):
        self.file_content = """
1234567890123|ABC123|100.5|2023-01-01|
9876543210987|XYZ789|200.75|2023-01-02|
1234567890123|ABC123|150.25|2023-01-03|
"""

    def test_import_command(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write(self.file_content)
            temp_file.flush()
            temp_file_path = temp_file.name

        try:
            out = StringIO()
            call_command('import_d0010', temp_file_path, stdout=out)
            self.assertIn('Successfully imported', out.getvalue())
            self.assertIn('Created 3 new readings', out.getvalue())

            # Check if data was imported correctly
            self.assertEqual(MeterPoint.objects.count(), 2)
            self.assertEqual(Meter.objects.count(), 2)
            self.assertEqual(Reading.objects.count(), 3)

            # Check specific reading
            reading = Reading.objects.get(meter__serial_number='ABC123', date='2023-01-01')
            self.assertEqual(reading.value, 100.5)

            # Test duplicate import
            out = StringIO()
            call_command('import_d0010', temp_file_path, stdout=out)
            self.assertIn('Created 0 new readings', out.getvalue())
            self.assertIn('Duplicate reading found', out.getvalue())
            self.assertEqual(Reading.objects.count(), 3)  # Count should not change

        finally:
            os.unlink(temp_file_path)

    def test_import_command_invalid_data(self):
        invalid_content = """
1234567890123|ABC123|invalid|2023-01-01|
9876543210987|XYZ789|200.75|invalid-date|
"""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file.write(invalid_content)
            temp_file.flush()
            temp_file_path = temp_file.name

        try:
            out = StringIO()
            call_command('import_d0010', temp_file_path, stdout=out)
            self.assertIn('Skipping row with invalid data', out.getvalue())
            self.assertEqual(Reading.objects.count(), 0)  # No readings should be created
        finally:
            os.unlink(temp_file_path)

    @patch('app.management.commands.import_d0010.open')
    def test_import_command_file_not_found(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        out = StringIO()
        call_command('import_d0010', 'non_existent_file.txt', stdout=out)
        self.assertIn('File not found', out.getvalue())

