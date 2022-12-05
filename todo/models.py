from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
