from django.urls import path
from ..views.api_views import ListCreateTasks, TaskDetailView


urlpatterns = [
    path("api/tasks/", ListCreateTasks.as_view(), name="tasks list"),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]