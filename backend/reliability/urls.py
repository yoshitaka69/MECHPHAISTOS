# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FailureDataViewSet, predict_failure, WeibullDataViewSet, BayesianPredictionViewSet,TroubleHistoryViewSet,CompanyCodeTroubleHistoryViewSet

router = DefaultRouter()
router.register(r'troubleHistory', TroubleHistoryViewSet, basename='troubleHistory')
router.register(r'troubleHistoryByCompany', CompanyCodeTroubleHistoryViewSet, basename='companyCode-troubleHistory')


#router.register(r'failuredata', FailureDataViewSet, basename='reliability')
router.register(r'weibull-data', WeibullDataViewSet)
router.register(r'bayesianPrediction', BayesianPredictionViewSet, basename='reliability')


urlpatterns = [
    path('reliability/', include(router.urls)),
    #path('reliability/predict/', predict_failure, name='predict_failure'),
    path('reliability/BayesianPrediction/', predict_failure, name='BayesianPrediction'),
]
