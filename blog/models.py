from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
    url = models.ImageField(upload_to='forthegram/')
    title = models.CharField(max_length=100)
    caption = models.TextField()
    likes = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
