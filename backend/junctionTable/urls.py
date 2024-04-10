from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (MasterDataTableViewSet,CompanyCodeMDTViewSet,
                    BomAndTaskViewSet,CompanyCodeBomAndTaskViewSet,CeListAndTaskViewSet,CompanyCodeCeListAndTaskViewSet,)


router = DefaultRouter()
router.register(r'masterDataTable', MasterDataTableViewSet, basename='masterDataTable')
router.register(r'masterDataTableByCompany', CompanyCodeMDTViewSet, basename='companyCode-masterDataTable')

router.register(r'bomAndTask', BomAndTaskViewSet, basename='bomAndTask')
router.register(r'bomAndTaskByCompany', CompanyCodeBomAndTaskViewSet, basename='companyCode-bomAndTask')

router.register(r'ceListAndTask', CeListAndTaskViewSet, basename='ceListAndTask')
router.register(r'ceListAndTaskByCompany', CompanyCodeCeListAndTaskViewSet, basename='companyCode-ceListAndTask')

urlpatterns = [
    path('junctionTable/', include(router.urls)),
]
