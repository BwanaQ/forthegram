from django.urls import path
from .views import (
    ImageListView,
    ImageDetailView,
    ImageCreateView,
    ImageUpdateView,
    ImageDeleteView
)
from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='blog-home'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('image/new/', ImageCreateView.as_view(), name='image-create'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='image-update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image-delete'),
    path('about/', views.about, name='blog-about'),

]
