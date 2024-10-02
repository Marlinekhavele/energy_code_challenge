import csv
from django.core.management.base import BaseCommand
from app.models import MeterPoint, Meter, Reading
from django.db import transaction
from django.core.exceptions import ValidationError
import datetime

class Command(BaseCommand):
    help = 'Import D0010 flow file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the D0010 file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file, delimiter='|')
                
                with transaction.atomic():
                    readings_created = 0
                    for row in reader:
                        if len(row) < 4:
                            self.stdout.write(self.style.WARNING(f"Skipping row with insufficient fields: {row}"))
                            continue
                        
                        mpan, meter_serial, reading_value, reading_date_str, *extra_fields = row
                        
                        if extra_fields:
                            self.stdout.write(self.style.WARNING(f"Row has extra fields which will be ignored: {extra_fields}"))
                        
                        try:
                            reading_value = float(reading_value)
                            reading_date = datetime.datetime.strptime(reading_date_str, '%Y-%m-%d').date()
                        except ValueError as e:
                            self.stdout.write(self.style.WARNING(f"Skipping row with invalid data: {row}. Error: {str(e)}"))
                            continue
                        
                        try:
                            meter_point, _ = MeterPoint.objects.get_or_create(mpan=mpan)
                            meter, _ = Meter.objects.get_or_create(meter_point=meter_point, serial_number=meter_serial)
                            
                            reading, created = Reading.objects.get_or_create(
                                meter=meter,
                                date=reading_date,
                                defaults={'value': reading_value, 'flow_file': file_path}
                            )
                            if created:
                                readings_created += 1
                            else:
                                self.stdout.write(self.style.WARNING(f"Duplicate reading found for meter {meter_serial} on {reading_date}. Skipping."))
                        except ValidationError as e:
                            self.stdout.write(self.style.ERROR(f"Validation error for row {row}: {str(e)}"))
            
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {file_path}. Created {readings_created} new readings.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while importing the file: {str(e)}"))








