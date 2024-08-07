from django.core.management.base import BaseCommand
import csv
from models import MeterPoint, Meter, Reading

class Command(BaseCommand):
    help = 'Import D0010 file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                mpan = row[0]
                serial_number = row[1]
                value = row[2]
                date = row[3]
                
                meter_point, created = MeterPoint.objects.get_or_create(mpan=mpan)
                meter, created = Meter.objects.get_or_create(meter_point=meter_point, serial_number=serial_number)
                Reading.objects.create(meter=meter, value=value, date=date, filename=file_path)

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {file_path}'))
