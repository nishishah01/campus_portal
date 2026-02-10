from django.urls import path
from .views import SaveSearchView
from .views import JobListView, UserSearchView

urlpatterns = [
    path("search/", SaveSearchView.as_view()),
    path("jobs/", JobListView.as_view()),
    path("searches/", UserSearchView.as_view()),
]
