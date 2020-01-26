from django.db import models
csCourses = [
    ("CSCE 111", "CSCE 111"),
    ("CSCE 121", "CSCE 121"),
    ("CSCE 206", "CSCE 206"),
    ("CSCE 221", "CSCE 221"),
    ("CSCE 222", "CSCE 222"),
    ("CSCE 312", "CSCE 312"),
    ("CSCE 313", "CSCE 313"),
    ("CSCE 314", "CSCE 314"),
    ("CSCE 315", "CSCE 315"),
    ("Other", "Other"),
]
# Create your models here.
class Tickets(models.Model):
    name = models.CharField("First Name", max_length=15)
    course = models.CharField(max_length=8, choices = csCourses)
    question = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    peer = models.CharField(max_length=50,null=True,default="none")
    timestamp = models.DateTimeField(auto_now_add= True)