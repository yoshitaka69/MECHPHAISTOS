from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlannedPM02ViewSet, ActualPM02ViewSet,PlannedPM03ViewSet, ActualPM03ViewSet, ActualPM04ViewSet,PlannedPM05ViewSet, ActualPM05ViewSet

router = DefaultRouter()
router.register(r'plannedPM02', PlannedPM02ViewSet, basename='plannedPM02')
router.register(r'actualPM02', ActualPM02ViewSet, basename='actualPM02')
router.register(r'plannedPM03', PlannedPM03ViewSet, basename='plannedPM03')
router.register(r'actualPM03', ActualPM03ViewSet, basename='actualPM03')

router.register(r'actualPM04', ActualPM04ViewSet, basename='actualPM04')
router.register(r'plannedPM05', PlannedPM05ViewSet, basename='plannedPM05')
router.register(r'actualPM05', ActualPM05ViewSet, basename='actualPM05')

urlpatterns = [
    path('repairingCost/', include(router.urls)),
]
