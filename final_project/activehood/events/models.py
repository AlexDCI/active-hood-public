from django.db import models
from django.contrib.auth.models import User
from locations.models import City
from users import choices 
from users.models import Activity

class Event(models.Model): 
    name = models.CharField(max_length=100, choices=choices.ACTIVITIES_CHOICES)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.ForeignKey(City, on_delete=models.CASCADE, null=True) #temporarily optional
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events') # from a User instance, you can access the events they created via user.created_events.all()
    participants = models.ManyToManyField(User, blank=True,related_name='participating_events') # from a User instance, you can access the events they are participating in via user.participating_events.all()
    
    def __str__(self):
        return f"{self.name}, {self.date}"