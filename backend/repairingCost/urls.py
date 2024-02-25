from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Pm02ViewSet, Pm03ViewSet, Pm04ViewSet, Pm05ViewSet

router = DefaultRouter()
router.register(r'pm02', Pm02ViewSet, basename='pm02')
router.register(r'pm03', Pm03ViewSet, basename='pm03')
router.register(r'pm04', Pm04ViewSet, basename='pm04')
router.register(r'pm05', Pm05ViewSet, basename='pm05')

urlpatterns = [
    path('repairingCost/', include(router.urls)),
]
