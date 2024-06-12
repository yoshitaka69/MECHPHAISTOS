from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FailureDataViewSet, predict_failure, WeibullDataViewSet



router = DefaultRouter()
router.register(r'failuredata', FailureDataViewSet, basename='reliability')
router.register(r'weibull-data', WeibullDataViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('reliability/predict/', predict_failure, name='predict_failure'),  # predict_failureビューを追加
]
