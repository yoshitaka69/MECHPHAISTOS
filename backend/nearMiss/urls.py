from django.urls import path
from nearMiss import views


urlpatterns = [
    path('nearMiss/', views.NearMissListView.as_view()),
]
