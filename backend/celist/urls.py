from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CeListViewSet, company_ce_list, CeListByCompanyViewSet

router = DefaultRouter()
router.register(r'ceList', CeListViewSet, basename='ceList')

urlpatterns = [
    path('ceList/', include(router.urls)),
    path('company-ce/', company_ce_list, name='company-ce'),
    path('ce-by-company/<str:companyCode_slug>/', CeListByCompanyViewSet.as_view({'get': 'list'}), name='ce-by-company')
]