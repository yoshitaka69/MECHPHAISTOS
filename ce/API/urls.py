from django.urls import path
from . import views



urlpatterns = [
    path('ce/',views.ListView.as_view(),name='list'),
    path('ce/<int:pk>/',views.DetailView.as_view(),name='detail'),

]