from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=100)
    career_url = models.URLField()

class UserSearch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Job(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    skills = models.TextField(null=True, blank=True)
    apply_link = models.URLField(null=True, blank=True)
    job_hash = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.title}"
