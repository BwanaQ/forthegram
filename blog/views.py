from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Image, Comment


def home(request):
    context = {
        'posts': Image.objects.all()
    }
    return render(request, 'blog/home.html', context)


class ImageListView(ListView):
    model = Image
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-timestamp']


class ImageDetailView(DetailView):
    model = Image


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
