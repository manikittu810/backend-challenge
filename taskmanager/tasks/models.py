from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    """
    Represents a label that can be attached to multiple tasks.
    Each label is unique to an owner and can be associated with multiple tasks.
    This uniqueness ensures that no two labels with the same name exist for the same owner.
    """
    # Stores the label name, must be unique within the scope of each user.
    name = models.CharField(max_length=100, unique=True)
    
    # ForeignKey links each label to a specific user (owner).
    # 'on_delete=models.CASCADE' means if a user is deleted, their labels are also deleted.
    owner = models.ForeignKey(User, related_name='labels', on_delete=models.CASCADE)

    def __str__(self):
        # Returns a string representation of the label, which is its name.
        return self.name

class Task(models.Model):
    """
    Represents a task created by a user. Tasks can have multiple labels and
    a status indicating whether they are completed.
    """
    # Title of the task, up to 200 characters.
    title = models.CharField(max_length=200)
    
    # A more detailed text description of the task.
    description = models.TextField()
    
    # Boolean field that indicates whether the task is completed.
    completion_status = models.BooleanField(default=False)
    
    # ForeignKey links each task to a user (owner). 
    # Tasks are deleted if the owner is deleted from the database.
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    
    # ManyToManyField creates a many-to-many relationship with Label.
    # A task can have many labels, and a label can be associated with many tasks.
    labels = models.ManyToManyField(Label, related_name='tasks')

    def __str__(self):
        # Returns the title of the task, used as the string representation.
        return self.title
