from django.core.mail import send_mail
from django.conf import settings

def send_job_alert(user, jobs):
    if not jobs:
        return

    message = "New job openings matching your search:\n\n"

    for job in jobs:
        message += f"""
Company: {job.company}
Role: {job.title}
Location: {job.location}
Job Type: {job.job_type}
Apply here: {job.apply_link}

-------------------------
"""

    send_mail(
        subject="🚀 New Job Alert",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )
