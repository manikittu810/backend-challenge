from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the Django admin interface.
    path('api/', include('tasks.urls')),  # Includes all URLs from the tasks app under the '/api/' prefix.
    path('', lambda request: redirect('api/')),  # Redirects the root URL ('/') to '/api/'.
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint for token authentication.
]
