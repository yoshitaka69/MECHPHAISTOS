from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SparePartsViewSet,CompanyCodeSPViewSet,BomcodeViewSet,CompanyBomCodeViewSet


router = DefaultRouter()
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')
router.register(r'sparePartsByCompany', CompanyCodeSPViewSet, basename='companyCode-spareParts')

router.register(r'bomCode', BomCodeViewSet, basename='bomCode')
router.register(r'bomCodeByCompany', CompanyBomCodeViewSet, basename='companyCode-bomCode')


urlpatterns = [
    path('spareParts/', include(router.urls)),
]
