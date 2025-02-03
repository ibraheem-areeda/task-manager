from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('register/',views.user_register, name="user register" ),
    path('login/',views.user_login, name="user login" ),
]