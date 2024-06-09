from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.photo, name='photo'),
    path('upload/', views.upload, name='upload'),
]