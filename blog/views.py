from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import Image, Comment
from django.shortcuts import render, get_object_or_404


class ImageListView(ListView):
    model = Image
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-timestamp']
    paginate_by = 2


class ImageDetailView(DetailView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects. all()
        return context


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'caption', 'url']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['title', 'caption', 'url']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.creator:
            return True
        return False


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = '/'

    def test_func(self):
        image = self.get_object()
        if self.request.user == image.creator:
            return True
        return False
