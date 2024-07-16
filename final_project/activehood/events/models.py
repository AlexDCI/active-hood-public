from django.db import models
from django.contrib.auth.models import User
from locations.models import City

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.ForeignKey(City, on_delete=models.CASCADE, null=True) #temporarily optional
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    #participation = models.ForeignKey(User, )
    
    def __str__(self):
        return self.name