from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SparePartsViewSet,CompanyCodeSPViewSet,BomListViewSet,CompanyBomListViewSet,SparePartsManagementViewSet,CompanySparePartsManagementViewSet


router = DefaultRouter()
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')
router.register(r'sparePartsByCompany', CompanyCodeSPViewSet, basename='companyCode-spareParts')

router.register(r'bomList', BomListViewSet, basename='bomCode')
router.register(r'bomListByCompany', CompanyBomListViewSet, basename='companyCode-bomCode')

router.register(r'sparePartsManagement', SparePartsManagementViewSet, basename='sparePartsManagement')
router.register(r'sparePartsManagementByCompany', CompanySparePartsManagementViewSet, basename='companyCode-sparePartsManagement')


urlpatterns = [
    path('spareParts/', include(router.urls)),
]
