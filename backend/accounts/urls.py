from django.urls import path
from .views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]
urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
]
