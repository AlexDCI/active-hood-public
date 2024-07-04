from django.db import models
from .choices import ACTIVITIES_CHOICES, CITY_CHOICES

class Activity(models.Model):
    name = models.CharField(max_length=100, choices=ACTIVITIES_CHOICES)
    
    def __str__(self):
        return self.name

class User(models.Model):
    # Personal information
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
    # Authentication
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # In practice, consider using Django's built-in password hashing
    
    # City in Germany
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    
    # Preferred activities (many-to-many relationship with Activity model)
    preferred_activities = models.ManyToManyField(Activity, blank=True)
    
    # Profile picture
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # About myself
    about_myself = models.TextField(blank=True)
    
    # Friends (many-to-many relationship with self)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
