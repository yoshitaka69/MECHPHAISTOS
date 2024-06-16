from django.urls import path
from . import views  # ここで views をインポート

urlpatterns = [
    path('', views.index, name='index'),
    path('api/canvas/', views.CanvasStateListCreate.as_view(), name='canvas_state_list_create'),
]
