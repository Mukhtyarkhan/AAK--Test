from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label, null=True, blank=True)

    def __str__(self):
        return self.title
    


