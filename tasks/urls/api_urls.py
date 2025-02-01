from django.urls import path
from ..views import api_views


urlpatterns = [

    path("api/tasks/", api_views.ListCreateTasks.as_view(), name="tasks list"),
]