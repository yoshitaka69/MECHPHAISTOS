from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Co2ViewSet, StmViewSet, ElectricityUsageViewSet, CompressedAirViewSet,WellWaterViewSet,PureWaterViewSet,WwtViewSet,ExhaustGasViewSet

router = DefaultRouter()
router.register(r'co2', Co2ViewSet, basename='co2')
router.register(r'stm', StmViewSet, basename='stm')
router.register(r'electricityUsage', ElectricityUsageViewSet, basename='electricityUsage')
router.register(r'compressedAir', CompressedAirViewSet, basename='compressedAir')
router.register(r'wellWater', WellWaterViewSet, basename='wellWater')
router.register(r'pureWater', PureWaterViewSet, basename='pureWater')
router.register(r'wwt', WwtViewSet, basename='wwt')
router.register(r'exhaustGas', ExhaustGasViewSet, basename='exhaustGas')

urlpatterns = [
    path('sustainability/', include(router.urls)),
]