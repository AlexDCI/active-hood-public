from django.db import models
from .choices import ACTIVITIES_CHOICES, CITY_CHOICES
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password


# class Activity(models.Model):
#     name = models.CharField(max_length=100, choices=ACTIVITIES_CHOICES)

#     def __str__(self):
#         return self.name


# class CustomUser(AbstractUser):
#     # Personal information
#     date_of_birth = models.DateField()
#     city = models.CharField(max_length=50, choices=CITY_CHOICES)

#     # Additional fields
#     profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
#     about_myself = models.TextField(blank=True)

#     # Relationships
#     preferred_activities = models.ManyToManyField(Activity, blank=True)
#     friends = models.ManyToManyField("self", symmetrical=True, blank=True)

#     groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
#     user_permissions = models.ManyToManyField(
#         Permission, related_name="custom_user_set", blank=True
#     )

#     def save(self, *args, **kwargs):
#         if self.password:
#             self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.username} ({self.get_full_name()})"
