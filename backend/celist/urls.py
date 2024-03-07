from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CeViewSet, company_ce_list, CeByCompanyViewSet

router = DefaultRouter()
router.register(r'ce', CeViewSet, basename='ce')

urlpatterns = [
    path('ceList/', include(router.urls)),
    path('company-ce/', company_ce_list, name='company-ce'),
    path('ce-by-company/<str:companyCode_slug>/', CeByCompanyViewSet.as_view({'get': 'list'}), name='ce-by-company')
]