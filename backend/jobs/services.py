from .models import UserSearch
from .matching import find_matching_jobs
from .email_utils import send_job_alert

def run_job_matching():
    searches = UserSearch.objects.select_related("user")

    for search in searches:
        matched_jobs = find_matching_jobs(search)
        send_job_alert(search.user, matched_jobs)
