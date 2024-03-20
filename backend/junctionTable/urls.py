from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MasterDataTableViewSet,CompanyCodeMDTViewSet


router = DefaultRouter()
router.register(r'masterDataTable', MasterDataTableViewSet, basename='masterDataTable')
router.register(r'masterDataTableByCompany', CompanyCodeMDTViewSet, basename='companyCode-masterDataTable')


urlpatterns = [
    path('junctionTable/', include(router.urls)),
]