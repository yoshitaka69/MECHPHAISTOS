from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipmentSpecificationViewSet,InspectionFormViewSet

router = DefaultRouter()
router.register(r'equipmentspecifications', EquipmentSpecificationViewSet)
router.register(r'inspection_forms', InspectionFormViewSet)

urlpatterns = [
    path('workingReport/', include(router.urls)),
]
