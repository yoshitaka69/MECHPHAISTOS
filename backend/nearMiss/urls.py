from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NearMissViewSet, CompanyNearMissViewSet, SafetyIndicatorsViewSet,CompanySafetyIndicatorsViewSet,TrendSafetyIndicatorsViewSet,CompanyTrendSafetyIndicatorsViewSet

# ルーターの設定
router = DefaultRouter()
router.register(r'nearMissList', NearMissViewSet, basename='nearMiss')
router.register(r'nearMissByCompany', CompanyNearMissViewSet, basename='companyCode-nearMiss')

router.register(r'safetyIndicators', SafetyIndicatorsViewSet, basename='safetyIndicators')
router.register(r'safetyIndicatorsByCompany', CompanySafetyIndicatorsViewSet, basename='companyCode-safetyIndicators')


router.register(r'trendSafetyIndicators', TrendSafetyIndicatorsViewSet, basename='trendSafetyIndicators')
router.register(r'trendSafetyIndicatorsByCompany', CompanyTrendSafetyIndicatorsViewSet, basename='companyCode-trendSafetyIndicators')


urlpatterns = [
    path('nearMiss/', include(router.urls)),
]
