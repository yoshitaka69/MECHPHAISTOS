from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (Co2ViewSet, CompanyCodeCo2ViewSet, 
                    StmViewSet, CompanyCodeStmViewSet,
                    ElecViewSet, CompanyCodeElecViewSet,
                    CompAirViewSet,CompanyCodeCompAirViewSet,
                    WellWaterViewSet,CompanyCodeWellWaterViewSet,
                    PureWaterViewSet,CompanyCodePureWaterViewSet,
                    WwtViewSet,CompanyCodeWwtViewSet,
                    ExhaustGasViewSet,CompanyCodeExhaustGasViewSet)

router = DefaultRouter()
router.register(r'co2', Co2ViewSet, basename='co2')
router.register(r'co2ByCompany', CompanyCodeCo2ViewSet, basename='companyCode-co2')

router.register(r'stm', StmViewSet, basename='stm')
router.register(r'stmByCompany', CompanyCodeStmViewSet, basename='companyCode-stm')

router.register(r'electricityUsage', ElecViewSet, basename='electricityUsage')
router.register(r'elecByCompany', CompanyCodeElecViewSet, basename='companyCode-elec')

router.register(r'compressedAir', CompAirViewSet, basename='compressedAir')
router.register(r'compAirByCompany', CompanyCodeCompAirViewSet, basename='companyCode-compAir')

router.register(r'wellWater', WellWaterViewSet, basename='wellWater')
router.register(r'wellWaterByCompany', CompanyCodeWellWaterViewSet, basename='companyCode-wellWater')

router.register(r'pureWater', PureWaterViewSet, basename='pureWater')
router.register(r'pureWaterByCompany', CompanyCodePureWaterViewSet, basename='companyCode-pureWater')

router.register(r'wwt', WwtViewSet, basename='wwt')
router.register(r'wwtByCompany', CompanyCodeWwtViewSet, basename='companyCode-wwt')

router.register(r'exhaustGas', ExhaustGasViewSet, basename='exhaustGas')
router.register(r'exhaustGasByCompany', CompanyCodeExhaustGasViewSet, basename='companyCode-exhaustGas')

urlpatterns = [
    path('sustainability/', include(router.urls)),
]
