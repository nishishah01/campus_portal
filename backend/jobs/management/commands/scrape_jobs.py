from django.core.management.base import BaseCommand
from jobs.firecrawl_service import scrape_career_page
from jobs.job_extractor import extract_and_save_jobs
from jobs.company_config import COMPANIES

class Command(BaseCommand):
    help = "Scrape company career pages"

    def handle(self, *args, **kwargs):
        for company, url in COMPANIES.items():
            self.stdout.write(f"Scraping {company}")
            text = scrape_career_page(url)
            extract_and_save_jobs(text, company)
