from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CeListViewSet,CeListByCompanyViewSet

router = DefaultRouter()
router.register(r'ceList', CeListViewSet, basename='ceList')
router.register(r'ceListByCompany', CeListByCompanyViewSet, basename='companyCode-ceList')


urlpatterns = [
    path('ceList/', include(router.urls)),
]