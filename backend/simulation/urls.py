from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BaseSimulationViewSet
from .views import No1SimulationViewSet
from .views import No2SimulationViewSet

from .views import No3SimulationViewSet


router = DefaultRouter()
router.register(r'BaseSimulations', BaseSimulationViewSet)
router.register(r'no1simulations', No1SimulationViewSet)
router.register(r'no2simulations', No2SimulationViewSet)
router.register(r'no3simulations', No3SimulationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]