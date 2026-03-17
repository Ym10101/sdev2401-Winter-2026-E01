from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from courses.models import Submission

class Command(BaseCommand):
    help = "Notify instructors about new submissions"

    def handle(self, *args, **kwargs):
        # Only fetch submissions not yet notified
        # We can avoid making this a N+1 query by selecting the related records when we make our first query call
        # This way we are not querying for the new submission then query for the assignment and querying for the owner
        # for each new submission found.

        # select_related will fetch the submissions + the related assignment and owner at the same time
        # assignment__owner means to follow 'assignment', then follow 'owner' 

        # We can select_related for multiple records if needed by comma separating the related links we want
        # Example: .select_related('assignment__owner', 'assignment__course')
        new_submissions = Submission.objects.filter(instructor_notified=False).select_related('assignment__owner')
        count = new_submissions.count()
        if count == 0:
            self.stdout.write(self.style.SUCCESS("No new submissions to notify instructors about"))
            return
        
        for submission in new_submissions:
            # since we already select_related on the main query
            # the submission.assignment.title and submission.assignment.owner are already in memory
            # we are not triggering another 2 queries to the database for the submission record
            instructor = submission.assignment.owner

            send_mail(
                subject='New Submission Received',
                message=f'{submission.assignment.title} has a new submission from {submission.student_name}',
                from_email='notifications@test.com',
                recipient_list=[instructor.email],
            )

            # Mark the submission as notified so it won't be processed again
            submission.instructor_notified = True
            submission.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully notified instructors about {count} new submissions'
            )
        )
