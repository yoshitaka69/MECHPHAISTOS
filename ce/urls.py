from django.urls import path
from . import views

app_name = 'ce'
urlpatterns = [
    # ここにアプリケーションごとの設定を記載する
    path('', views.CeList.as_view(), name='list'),
    #↑テスト
]