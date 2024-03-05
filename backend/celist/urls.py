from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CeViewSet, SparePartsViewSet, TaskViewSet,company_ce_list,CeByCompanyViewSet

router = DefaultRouter()
router.register(r'ce', CeViewSet, basename='ce')
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('ceList/', include(router.urls)),
    path('company-ce/', company_ce_list, name='company-ce'),
    path('ce-by-company/<str:companyCode_slug>/', CeByCompanyViewSet.as_view({'get': 'list'}), name='ce-by-company')
]