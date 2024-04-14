from django.http import HttpResponse
# Assuming 'home' is defined in 'taskmanager/views.py'

def home(request):
    return HttpResponse("Welcome to the Task Manager API!")
