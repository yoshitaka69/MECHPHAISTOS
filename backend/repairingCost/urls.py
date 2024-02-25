from django.urls import path
from repairingCost import views


urlpatterns = [
    path('repairingCost/pm02', views.Pm02View.as_view()),
    path('repairingCost/pm03', views.Pm03View.as_view()),
    path('repairingCost/pm04', views.Pm04View.as_view()),
    path('repairingCost/pm05', views.Pm05View.as_view()),
]