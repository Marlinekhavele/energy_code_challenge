from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import D0010 files'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to D0010 file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.stdout.write(self.style.SUCCESS('Successfully imported D0010 file'))

# where is the file path 
# where is the data should be stored on the db 
# error handling on wron files 
# we can import the files from the machine locally