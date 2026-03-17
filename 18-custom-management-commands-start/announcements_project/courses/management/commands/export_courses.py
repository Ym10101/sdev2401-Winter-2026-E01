import csv
from django.core.management.base import BaseCommand, CommandParser
from courses.models import Course

class Command(BaseCommand):
    help = 'Export courses to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'output_path',
            type=str,
            help='The path to the output CSV file'
        )

    def handle(self, *args, **kwargs):
        output_path = kwargs.get('output_path')
        if not output_path:
            self.stdout.write(self.style.ERROR('Please provide an output path'))
            return

        courses = Course.objects.all()
        with open(output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title','description']) #Write the header first row
            for course in courses:
                writer.writerow([course.title,course.description])

        self.stdout.write(self.style.SUCCESS(
            f'Successfully exported {len(courses)} courses to "{output_path}"'))
