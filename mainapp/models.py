from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=250)
    taskMessage=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.taskTitle} - {self.taskMessage} - {self.created}"