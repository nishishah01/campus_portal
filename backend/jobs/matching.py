from .models import Job

def find_matching_jobs(user_search):
    jobs = Job.objects.all()
    matched = []

    for job in jobs:
        # Role match
        if user_search.role.lower() not in job.title.lower():
            continue

        # Location match
        if user_search.location.lower() not in job.location.lower():
            continue

        # Company match (if user specified one)
        if user_search.company:
            if user_search.company.lower() not in job.company.lower():
                continue

        # Skills match (optional, basic)
        if user_search.skills and job.skills:
            user_skills = [s.strip().lower() for s in user_search.skills.split(",")]
            job_skills = job.skills.lower()

            if not any(skill in job_skills for skill in user_skills):
                continue

        matched.append(job)

    return matched
