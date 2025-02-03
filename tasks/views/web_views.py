from django.shortcuts import render
from ..models import Task


def tasks_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "task_list.html", {"tasks": tasks})

def tasks_form(request):
    return render(request, "task_form.html")