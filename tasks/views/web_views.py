from django.shortcuts import redirect, render
from ..models import Task
from ..forms import CreateTaskForm


def tasks_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "task_list.html", {"tasks": tasks})

def tasks_details(request,id):
    task = Task.objects.get(id=id)
    return render(request, "tasks_details.html", {"task": task})

def tasks_form(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks:tasks_list")
    else:
        form = CreateTaskForm()
    return render(request, "task_form.html",{ "form": form })

def tasks_update(request,id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:tasks_list")
    else:
        form = CreateTaskForm(instance=task)
    return render(request, "task_update.html", { "form": form })

def tasks_delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("tasks:tasks_list")		