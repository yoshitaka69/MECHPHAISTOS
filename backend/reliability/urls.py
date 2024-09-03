# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReliabilityViewSet,CompanyCodeReliabilityViewSet,TroubleHistoryViewSet,CompanyCodeTroubleHistoryViewSet,FailurePredictionPointViewSet,CompanyCodeFPPViewSet


router = DefaultRouter()
router.register(r'reliability', ReliabilityViewSet, basename='reliability')
router.register(r'reliabilityByCompany', CompanyCodeReliabilityViewSet, basename='companyCode-reliability')


router.register(r'troubleHistory', TroubleHistoryViewSet, basename='troubleHistory')
router.register(r'troubleHistoryByCompany', CompanyCodeTroubleHistoryViewSet, basename='companyCode-troubleHistory')

router.register(r'failurePredictionPoint', FailurePredictionPointViewSet, basename='failurePredictionPoint')
router.register(r'failurePredictionPointByCompany', CompanyCodeFPPViewSet, basename='companyCode-failurePredictionPoint')



urlpatterns = [
    path('reliability/', include(router.urls)),
]
