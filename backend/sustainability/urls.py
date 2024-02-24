from django.urls import path
from sustainability import views


urlpatterns = [
    path('sustainability/co2List', views.Co2ListView.as_view()),
    path('sustainability/stmList', views.StmListView.as_view()),
    path('sustainability/electricityUsage', views.StmListView.as_view()),
    path('sustainability/compressedAir', views.CompressedAirView.as_view()),
    path('sustainability/wellWater', views.WellWaterView.as_view()),
    path('sustainability/pureWater', views.PureWaterView.as_view()),
    path('sustainability/wwt', views.WwtView.as_view()),
    path('sustainability/exhaustGas', views.ExhaustGasView.as_view()),
]