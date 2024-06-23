from django.urls import path
from . import views

urlpatterns = [
    path('upload_audio/', views.upload_audio, name='upload_audio'),  # 他のURLパターンもここに追加
]
