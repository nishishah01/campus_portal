import hashlib
from .models import Job

ROLE_KEYWORDS = [
    "intern", "engineer", "developer", "data", "analyst", "software"
]

LOCATION_KEYWORDS = [
    "india", "bangalore", "bengaluru", "hyderabad",
    "pune", "mumbai", "delhi", "remote"
]

def extract_and_save_jobs(text, company):
    lines = text.split("\n")

    for line in lines:
        line_lower = line.lower()

        if any(role in line_lower for role in ROLE_KEYWORDS) and \
           any(loc in line_lower for loc in LOCATION_KEYWORDS):

            title = line.strip()
            location = "India"

            job_hash = hashlib.sha256(
                f"{company}{title}{location}".encode()
            ).hexdigest()

            Job.objects.get_or_create(
                job_hash=job_hash,
                defaults={
                    "company": company,
                    "title": title,
                    "location": location,
                    "job_type": "Internship" if "intern" in line_lower else "Full-Time",
                }
            )
