from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (MasterDataTableViewSet,CompanyCodeMDTViewSet,
                    BomAndTaskViewSet,CompanyCodeBomAndTaskViewSet,
                    AlertScheduleViewSet,CompanyCodeAlertScheduleViewSet)


router = DefaultRouter()
router.register(r'masterDataTable', MasterDataTableViewSet, basename='masterDataTable')
router.register(r'masterDataTableByCompany', CompanyCodeMDTViewSet, basename='companyCode-masterDataTable')

router.register(r'bomAndTask', BomAndTaskViewSet, basename='bomAndTask')
router.register(r'bomAndTaskByCompany', CompanyCodeBomAndTaskViewSet, basename='companyCode-bomAndTask')

router.register(r'alertSchedule', AlertScheduleViewSet, basename='alertSchedule')
router.register(r'alertScheduleByCompany', CompanyCodeAlertScheduleViewSet, basename='companyCode-alertSchedule')

urlpatterns = [
    path('junctionTable/', include(router.urls)),
]
