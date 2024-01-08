from django.urls import path,include
from celist import views


urlpatterns = [
    path('latest-celist/', views.LatestCeList.as_view()),
]

