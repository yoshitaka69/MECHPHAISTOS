from django.urls import path
from . import views

urlpatterns = [
    path('api/upload_audio/', views.upload_audio, name='upload_audio'),
]
