from rest_framework import viewsets
from .models import Task, Label
from .serializers import TaskSerializer, LabelSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions to be performed on Task model instances.
    It restricts the queryset to tasks owned by the currently authenticated user.
    """
    queryset = Task.objects.all()  # Initial queryset for tasks, will be filtered in get_queryset.
    serializer_class = TaskSerializer  # Specifies the serializer to use for tasks.

    def get_queryset(self):
        """
        This method customizes the queryset to return only the tasks that belong
        to the currently authenticated user, enhancing data security by ensuring users
        can only access their own task data.
        """
        return self.queryset.filter(owner=self.request.user)  # Filters the initial queryset by owner.

class LabelViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on the Label model, similar to TaskViewSet,
    but for labels. It ensures that only labels owned by the authenticated user are accessible.
    """
    queryset = Label.objects.all()  # Initial queryset for labels, will be filtered in get_queryset.
    serializer_class = LabelSerializer  # Specifies the serializer to use for labels.

    def get_queryset(self):
        """
        Customizes the queryset to include only labels that are owned by the currently
        authenticated user, maintaining privacy and security by restricting data access.
        """
        return self.queryset.filter(owner=self.request.user)  # Filters the initial queryset by owner.
