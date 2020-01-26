from django.db import models

# Create your models here.
class Tickets(models.Model):
    name = models.CharField(max_length=15)
    course = models.CharField(max_length=8)
    question = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    peer = models.CharField(max_length=50,null=True,default="none")
    timestamp = models.DateTimeField(auto_now_add= True)