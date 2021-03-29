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

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return str(time.hour - self.created_at.hour) + " hours ago"
        else:
            if self.created_at.month == time.month:
                return str(time.day - self.created_at.day) + " days ago"
            else:
                if self.created_at.year == time.year:
                    return str(time.month - self.created_at.month) + " months ago"
        return self.created_at


class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
