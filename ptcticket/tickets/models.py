from django.db import models
csCourses = [
    ('206', '206'),
    ('207', '207'),
    ('208', '208'),
    ('209', '209'),
]
# Create your models here.
class Tickets(models.Model):
    name = models.CharField(max_length=15)
    course = models.CharField(max_length=8, choices = csCourses)
    question = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add= True)