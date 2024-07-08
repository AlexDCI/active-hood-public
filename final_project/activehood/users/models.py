from django.db import models
from django.contrib.auth.models import User
from users.signals import *  # Import signals from separate file

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

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
