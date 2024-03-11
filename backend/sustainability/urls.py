from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Co2ViewSet, CompanyCodeCo2ViewSet, StmViewSet, ElectricityUsageViewSet, CompressedAirViewSet,WellWaterViewSet,PureWaterViewSet,WwtViewSet,ExhaustGasViewSet

router = DefaultRouter()
router.register(r'co2', Co2ViewSet, basename='co2')
router.register(r'companyCode-co2', CompanyCodeCo2ViewSet, basename='companyCode-co2')
router.register(r'stm', StmViewSet, basename='stm')
router.register(r'companyCode-stm', CompanyCodeStmViewSet, basename='companyCode-stm')
router.register(r'electricityUsage', ElectricityUsageViewSet, basename='electricityUsage')
router.register(r'companyCode-elec', CompanyCodeElectricityUsageViewSet, basename='companyCode-elec')
router.register(r'compressedAir', CompressedAirViewSet, basename='compressedAir')
router.register(r'companyCode-compAir', CompanyCodeCompressedViewSet, basename='companyCode-compAir')
router.register(r'wellWater', WellWaterViewSet, basename='wellWater')
router.register(r'companyCode-wellWater', CompanyCodeWellWaterViewSet, basename='companyCode-wellWater')
router.register(r'pureWater', PureWaterViewSet, basename='pureWater')
router.register(r'companyCode-pureWater', CompanyCodePureWaterViewSet, basename='companyCode-pureWater')
router.register(r'wwt', WwtViewSet, basename='wwt')
router.register(r'companyCode-wwt', CompanyCodeWwtViewSet, basename='companyCode-wwt')
router.register(r'exhaustGas', ExhaustGasViewSet, basename='exhaustGas')
router.register(r'companyCode-exhaustGas', CompanyCodeExhaustGasViewSet, basename='companyCode-exhaustGas')

urlpatterns = [
    path('sustainability/', include(router.urls)),
]
