from rest_framework import viewsets
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
