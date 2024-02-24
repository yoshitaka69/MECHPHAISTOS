from django.urls import path
from ceList import views


urlpatterns = [
    path('ceList/', views.CeListView.as_view()),
    path('ceList/sparePartsList', views.SparePartsListView.as_view()),
    path('ceList/taskList', views.TaskListView.as_view()),
]