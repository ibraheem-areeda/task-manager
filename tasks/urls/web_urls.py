from django.urls import path
from ..views import web_views


urlpatterns = [
    path("tasks-list/", web_views.tasks_list, name="tasks list"),
    path("tasks-form/", web_views.tasks_form, name="tasks form"),
    path("tasks-details/<int:id>/", web_views.tasks_details, name="tasks details"),
    path("tasks-update/<int:id>/", web_views.tasks_update, name="tasks update"),
    path("tasks-delete/<int:id>/", web_views.tasks_delete, name="tasks delete"),
]