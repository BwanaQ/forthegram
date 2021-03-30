from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(default='default_fiis58.jpg',
                              upload_to='forthegram_profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
