from django.db import models

# Create your models here.
class Tickets(models.Model):
    name = models.CharField(max_length=15)
    course = models.CharField(max_length=8)
    question = models.CharField(max_length=200)
    completed = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add= True)