from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Todo(models.Model):
    assignment = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('todo:todo-create')
