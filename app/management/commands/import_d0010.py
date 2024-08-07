from django.core.management.base import BaseCommand
import csv
from decimal import Decimal
from app.models import MeterPoint, Meter, Reading

class Command(BaseCommand):
    help = 'Import D0010 file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    # Skip irrelevant rows
                    if len(row) < 4 or not row[0].isdigit():
                        self.stderr.write(self.style.ERROR(f'Invalid row: {row}'))
                        continue

                    try:
                        mpan = row[0]
                        serial_number = row[1]
                        value = Decimal(row[2])
                        date = row[3]

                        meter_point, created = MeterPoint.objects.get_or_create(mpan=mpan)
                        meter, created = Meter.objects.get_or_create(meter_point=meter_point, serial_number=serial_number)
                        Reading.objects.create(meter=meter, value=value, date=date, filename=file_path)
                    except (ValueError, Decimal.InvalidOperation) as e:
                        self.stderr.write(self.style.ERROR(f'Error processing row {row}: {e}'))
                        continue

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {file_path}'))
        except IOError as e:
            self.stderr.write(self.style.ERROR(f'Error reading file {file_path}: {e}'))