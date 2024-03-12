from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlannedPM02ViewSet, CompanyCodePPM02ViewSet, ActualPM02ViewSet, CompanyCodeAPM02ViewSet, PlannedPM03ViewSet, CompanyCodePPM03ViewSet,ActualPM03ViewSet, CompanyCodeAPM03ViewSet, ActualPM04ViewSet, CompanyCodeAPM04ViewSet,PlannedPM05ViewSet,CompanyCodePPM05ViewSet, ActualPM05ViewSet,CompanyCodeAPM05ViewSet

router = DefaultRouter()
router.register(r'plannedPM02', PlannedPM02ViewSet, basename='plannedPM02')
router.register(r'companyCode-PPM02', CompanyCodePPM02ViewSet, basename='companyCode-PPM02')

router.register(r'actualPM02', ActualPM02ViewSet, basename='actualPM02')
router.register(r'companyCode-APM02', CompanyCodeAPM02ViewSet, basename='companyCode-APM02')

router.register(r'plannedPM03', PlannedPM03ViewSet, basename='plannedPM03')
router.register(r'companyCode-PPM03', CompanyCodePPM03ViewSet, basename='companyCode-PPM03')

router.register(r'actualPM03', ActualPM03ViewSet, basename='actualPM03')
router.register(r'companyCode-APM03', CompanyCodeAPM03ViewSet, basename='companyCode-APM03')

router.register(r'actualPM04', ActualPM04ViewSet, basename='actualPM04')
router.register(r'companyCode-APM04', CompanyCodeAPM04ViewSet, basename='companyCode-APM04')

router.register(r'plannedPM05', PlannedPM05ViewSet, basename='plannedPM05')
router.register(r'companyCode-PPM05', CompanyCodePPM05ViewSet, basename='companyCode-PPM05')

router.register(r'actualPM05', ActualPM05ViewSet, basename='actualPM05')
router.register(r'companyCode-APM05', CompanyCodeAPM05ViewSet, basename='companyCode-APM05')


urlpatterns = [
    path('repairingCost/', include(router.urls)),
]
