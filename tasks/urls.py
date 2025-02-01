from django.urls import include, path

urlpatterns = [
    path('', include('tasks.urls.web_urls')),
    path('api/', include('tasks.urls.api_urls')),
]