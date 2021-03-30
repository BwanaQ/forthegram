from django.urls import path
from .views import ImageListView, ImageDetailView
from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='blog-home'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('about/', views.about, name='blog-about'),
]
