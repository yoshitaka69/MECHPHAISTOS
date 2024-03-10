from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SparePartsViewSet, company_spareParts_list, SparePartsByCompanyViewSet

router = DefaultRouter()
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')

urlpatterns = [
    path('spareParts/', include(router.urls)),
    path('company-spareParts/', company_spareParts_list, name='company-spareParts'),
    path('spareParts-by-company/<str:companyCode_slug>/', SparePartsByCompanyViewSet.as_view({'get': 'list'}), name='spareParts-by-company')
]