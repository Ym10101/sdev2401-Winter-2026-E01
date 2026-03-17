import csv
from django.core.management.base import BaseCommand, CommandParser
from courses.models import Course

class Command(BaseCommand):
    help = 'Import courses from a CSV file into the database'

    def add_arguments(self, parser):
        # define any command line arguments
        # Adding one positional argument
        parser.add_argument(
            'csv_file',
            type=str,
            help='The path to the CSV file to import courses from'
        )
        # Adding as a optional argument
        # parser.add_argument(
        #     '--csv_file',
        #     type=str,
        #     required=False,
        #     default=None,
        #     help='The path to the CSV file to import courses from'
        # )
        pass
    
    def handle(self, *args, **kwargs):
        # the main logic of the command
        csv_file = kwargs.get('csv_file')
        if not csv_file:
            self.stdout.write(self.style.ERROR('Please provide a CSV file path'))
            return
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                _, created = Course.objects.get_or_create(
                    title = row['title'],
                    description = row['description']
                )
                if created:
                    count += 1
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {count} course(s) from "{csv_file}"'
        ))
        pass