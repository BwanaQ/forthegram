from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Comment
from datetime import datetime


def home(request):
    now = datetime.now()
    context = {
        'posts': Image.objects.all(),
        'now': now
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
