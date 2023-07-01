from django.db import models

# Create your models here.


class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(blank=True, null=True)
    tags = models.TextField(max_length=1000)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.title
