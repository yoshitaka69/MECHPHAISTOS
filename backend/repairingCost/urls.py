from django.urls import path
from repairingCost import views


urlpatterns = [
    path('repairingCost/pm02', views.RepairingCostPM02View.as_view()),
]