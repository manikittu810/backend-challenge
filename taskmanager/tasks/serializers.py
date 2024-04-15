from rest_framework import serializers
from .models import Task, Label

class LabelSerializer(serializers.ModelSerializer):
    """
    Serializer for the Label model.
    Transforms Label model instances into JSON format and handles
    incoming data to create or update Label instances.
    """
    class Meta:
        model = Label  # Specifies the Django model to serialize.
        fields = ['id', 'name', 'owner']  # Defines which fields should be included in the serialized output.

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    Includes nested LabelSerializer to handle the serialization of
    the labels associated with a task. This nested serializer makes
    the labels field read-only, meaning it will be included in
    responses but not processed from input during create/update operations.
    """
    # Nested LabelSerializer to serialize the many-to-many relationship with labels.
    # The 'many=True' indicates it is a many-to-many field.
    # 'read_only=True' ensures that label data can only be read, not written.
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Task  # Specifies the Django model to serialize.
        fields = ['id', 'title', 'description', 'completion_status', 'owner', 'labels']
        # Lists fields that should be included in the serialized output. Including 'labels' here
        # means the serialized data will include detailed label info, not just IDs.
