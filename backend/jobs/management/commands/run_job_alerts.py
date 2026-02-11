from django.core.management.base import BaseCommand
from jobs.company_config import COMPANIES
from jobs.firecrawl_service import scrape_career_page
from jobs.job_extractor import extract_and_save_jobs
from jobs.matching import find_matching_jobs

class Command(BaseCommand):
    help = "Run job scraping + matching + notifications"

    def handle(self, *args, **kwargs):
        self.stdout.write("🔍 Starting job alert pipeline")

        for company, url in COMPANIES.items():
            self.stdout.write(f"Scraping {company}")
            text = scrape_career_page(url)
            extract_and_save_jobs(text, company)

        self.stdout.write("🔗 Running matching logic")
        find_matching_jobs

        self.stdout.write("✅ Job alert cycle completed")
# This single command:
# Scrapes companies
# Saves jobs
# Runs matching
# Sends emails