from .web_urls import urlpatterns as web_patterns
from .api_urls import urlpatterns as api_patterns

app_name = 'tasks'
urlpatterns = web_patterns + api_patterns
