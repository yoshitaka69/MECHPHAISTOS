from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CeViewSet, SparePartsViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'ce', CeViewSet, basename='ce')
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('ceList/', include(router.urls)),
]