from django.urls import path
from ..views import web_views


urlpatterns = [
    path("tasks/list/", web_views.tasks_list, name="tasks_list"),
    path("tasks/form/", web_views.tasks_form, name="tasks_form"),
    path("tasks/details/<int:id>/", web_views.tasks_details, name="tasks_details"),
    path("tasks/update/<int:id>/", web_views.tasks_update, name="tasks_update"),
    path("tasks/delete/<int:id>/", web_views.tasks_delete, name="tasks_delete"),
]