from django.urls import path

from . import views

urlpatterns = [
    path("list", views.tasks_list, name="tasks list"),
    path("form", views.tasks_form, name="tasks form"),
]