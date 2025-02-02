from django.urls import path
from ..views import web_views


urlpatterns = [
    path("tasks/list/", web_views.tasks_list, name="tasks list"),
    path("tasks/form/", web_views.tasks_form, name="tasks form"),
]