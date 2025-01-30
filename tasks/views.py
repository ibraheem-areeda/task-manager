from django.shortcuts import render
from django.http import HttpResponse

def tasks_list(request):
    return render(request, "task_management/task_list.html")

def tasks_form(request):
    return render(request, "task_management/task_form.html")