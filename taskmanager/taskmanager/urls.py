from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', lambda request: redirect('api/')),  # Redirects root URL to /api/
]
