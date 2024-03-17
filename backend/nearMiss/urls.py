from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NearMissViewSet, CompanyNearMissViewSet, ActionItemListViewSet, SafetyIndicatorsViewSet

# ルーターの設定
router = DefaultRouter()
router.register(r'nearMissList', NearMissViewSet, basename='nearMiss')
router.register(r'nearMissByCompany', CompanyNearMissViewSet, basename='companyCode-nearMiss')
router.register(r'actionItemsList', ActionItemListViewSet, basename='actionItemList')
router.register(r'safetyIndicators', SafetyIndicatorsViewSet, basename='safetyIndicators')

urlpatterns = [
    path('nearMiss/', include(router.urls)),
]
