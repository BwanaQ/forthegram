from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Image(models.Model):
    url = models.ImageField(upload_to='forthegram/')
    title = models.CharField(max_length=100)
    caption = models.TextField()
    likes = models.IntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
