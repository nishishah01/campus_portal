from django.core.management.base import BaseCommand
from jobs.services import run_job_matching

class Command(BaseCommand):
    help = "Match jobs with user searches and send email alerts"

    def handle(self, *args, **kwargs):
        run_job_matching()
        self.stdout.write(self.style.SUCCESS("Job matching completed"))
