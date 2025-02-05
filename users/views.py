from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login,logout

def user_register(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            login(request, form.save())
            return redirect("tasks:tasks_list")
    else:
        form = UserCreationForm()
    return render(request, "user_register.html", { "form": form })

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("tasks:tasks_list")
    else:
        form = AuthenticationForm()
    return render(request, "user_login.html", {"form": form})

def user_logout(request):
    if request.method == "POST":
        logout(request)
    return redirect("/")
