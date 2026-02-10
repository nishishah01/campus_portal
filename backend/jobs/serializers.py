from rest_framework import serializers
from .models import UserSearch
from .models import Job, UserSearch

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearch
        fields = ["id", "company", "role", "location", "skills", "created_at"]