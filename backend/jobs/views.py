from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSearchSerializer
from .models import Job, UserSearch
from .serializers import JobSerializer, UserSearchSerializer

class SaveSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response({"message": "Search saved"})


class JobListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.all().order_by("-created_at")
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


class UserSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        searches = UserSearch.objects.filter(user=request.user)
        serializer = UserSearchSerializer(searches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
