from django.shortcuts import render

def user_register(request):
    print("User register view")
    return render(request, "user_register.html")




