from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CalTablePPM02ViewSet,CompanyCodeCalTablePPM02ViewSet,
                    CalTableAPM02ViewSet,CompanyCodeCalTableAPM02ViewSet,
                    CalTablePPM03ViewSet,CompanyCodeCalTablePPM03ViewSet,
                    CalTableAPM03ViewSet,CompanyCodeCalTableAPM03ViewSet,
                    CalTableAPM04ViewSet,CompanyCodeCalTableAPM04ViewSet,
                    CalTablePPM05ViewSet,CompanyCodeCalTablePPM05ViewSet,
                    CalTableAPM05ViewSet,CompanyCodeCalTableAPM05ViewSet,
                    SummedCostViewSet,CompanyCodeSummedCostViewSet)



router = DefaultRouter()


router.register(r'calTablePPM02', CalTablePPM02ViewSet, basename='calTablePPM02')
router.register(r'calTablePPM02ByCompany', CompanyCodeCalTablePPM02ViewSet, basename='companyCode-calTablePPM02')
router.register(r'calTableAPM02Cost', CalTableAPM02ViewSet, basename='calTableAPM02Cost')
router.register(r'calTableAPM02ByCompany', CompanyCodeCalTableAPM02ViewSet, basename='companyCode-calTableAPM02Cost')


router.register(r'CalTablePPM03', CalTablePPM03ViewSet, basename='CalTablePPM03')
router.register(r'CalTablePPM03ByCompany', CompanyCodeCalTablePPM03ViewSet, basename='companyCode-CalTablePPM03')
router.register(r'CalTableAPM03', CalTableAPM03ViewSet, basename='CalTableAPM03')
router.register(r'CalTableAPM03ByCompany', CompanyCodeCalTableAPM03ViewSet, basename='companyCode-CalTableAPM03')


router.register(r'CalTableAPM04', CalTableAPM04ViewSet, basename='CalTableAPM04')
router.register(r'CalTableAPM04ByCompany', CompanyCodeCalTableAPM04ViewSet, basename='companyCode-CalTableAPM04')


router.register(r'CalTablePPM05', CalTablePPM05ViewSet, basename='CalTablePPM05')
router.register(r'CalTablePPM05ByCompany', CompanyCodeCalTablePPM05ViewSet, basename='companyCode-CalTablePPM05')
router.register(r'CalTableAPM05', CalTableAPM05ViewSet, basename='CalTableAPM05')
router.register(r'CalTableAPM05dByCompany', CompanyCodeCalTableAPM05ViewSet, basename='companyCode-CalTableAPM05')

router.register(r'summedCost', SummedCostViewSet, basename='summedCost')
router.register(r'summedByCompany', CompanyCodeSummedCostViewSet, basename='companyCode-summedCost')


urlpatterns = [
    path('calculation/', include(router.urls)),
]