from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Comment

posts = [
    {
        'id': 1,
        'author': 'BwanaQ',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2020'
    },
    {
        'id': 2,
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 27, 2021'
    },
    {
        'id': 3,
        'author': 'Loise Hunja',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'March 2, 2021'
    }
]


def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
