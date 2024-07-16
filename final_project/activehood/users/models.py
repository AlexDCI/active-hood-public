from django.db import models
from django.contrib.auth.models import User, Group, Permission
from PIL import Image
from PIL import Image, UnidentifiedImageError
from django.db import models
from django.conf import settings
import os
from users.choices import CITY_CHOICES, ACTIVITIES_CHOICES, LEVEL_CHOICES
from locations.models import City


class Activity(models.Model):
    name = models.CharField(max_length=100, choices=ACTIVITIES_CHOICES)

    def __str__(self):
        return self.name

class ProfileActivity(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=50,choices=LEVEL_CHOICES,blank=True,null=True)


    def __str__(self):
        return f"{self.profile.user.username} - {self.activity.name} - {self.skill_level}"
    
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    preferred_activities = models.ManyToManyField(Activity, through=ProfileActivity, blank=True)
    friends = models.ManyToManyField("self", symmetrical=True, blank=True)
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(
         Permission, related_name="custom_user_set", blank=True
         )
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            
            img = Image.open(self.avatar.path)

            # Resize only if image is larger than 100x100 pixels
            if img.height > 100 or img.width > 100:
                new_img_size = (100, 100)
                img.thumbnail(new_img_size, Image.ANTIALIAS)
                img.save(self.avatar.path)

        except UnidentifiedImageError:
            # Handle the case where the image file cannot be identified
            # Log the error or use a default image instead
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default.jpg')
            img = Image.open(default_image_path)
            img.save(self.avatar.path)

        except Exception as e:
            # Handle other exceptions if necessary
            print(f"Error saving profile image: {e}")



# class CustomUser(AbstractUser):
#     # Personal information
#     date_of_birth = models.DateField()
#     
# city = models.CharField(max_length=50, choices=CITY_CHOICES)

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
