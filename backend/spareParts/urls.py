from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SparePartsViewSet,CompanyCodeSPViewSet,CategoryViewSet,LocationViewSet,ClassificationViewSet


router = DefaultRouter()
router.register(r'spareParts', SparePartsViewSet, basename='spareParts')
router.register(r'companyCode-spareParts', CompanyCodeSPViewSet, basename='companyCode-spareParts')

router.register(r'category', CategoryViewSet, basename='category')
router.register(r'location', LocationViewSet, basename='location')
router.register(r'classification', ClassificationViewSet, basename='classification')



urlpatterns = [
    path('spareParts/', include(router.urls)),
]