from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkOrderViewSet,WorkPermissionViewSet,WorkOrderManagementViewSet,CompanyCodeWorkOrderViewSet,CompanyCodeWorkPermissionViewSet,CompanyCodeWorkOrderManagementViewSet



router = DefaultRouter()
router.register(r'workOrder', WorkOrderViewSet, basename='workOrder')
router.register(r'workOrderByCompany', CompanyCodeWorkOrderViewSet, basename='companyCode-workOrder')

router.register(r'workPermission', WorkPermissionViewSet, basename='workPermission')
router.register(r'workPermissionByCompany', CompanyCodeWorkPermissionViewSet, basename='companyCode-workPermission')

router.register(r'workOrderManagement', WorkOrderManagementViewSet, basename='workOrderManagement')
router.register(r'workOrderManagementByCompany', CompanyCodeWorkOrderManagementViewSet, basename='companyCode-workOrderManagement')


urlpatterns = [
    path('workOrder/', include(router.urls)),
]


