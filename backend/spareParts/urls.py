from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SparePartsViewSet,CompanyCodeSPViewSet


router = DefaultRouter()
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')
router.register(r'sparePartsByCompany', CompanyCodeSPViewSet, basename='companyCode-spareParts')


urlpatterns = [
    path('spareParts/', include(router.urls)),
]