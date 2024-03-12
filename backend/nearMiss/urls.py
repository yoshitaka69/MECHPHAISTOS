from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NearMissViewSet, NearMissByCompanyViewSet

# ルーターの設定
router = DefaultRouter()
router.register(r'nearmiss', NearMissViewSet, basename='nearMiss')
router.register(r'companyCode-nearMiss', NearMissByCompanyViewSet, basename='companyCode-nearMiss')

urlpatterns = [
    path('', include(router.urls)),
]
