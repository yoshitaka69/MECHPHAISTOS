from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NearMissViewSet, NearMissByCompanyViewSet

router = DefaultRouter()
router.register(r'nearMiss', NearMissViewSet, basename='nearMiss')
#router.register(r'nearMiss', NearMissByCompanyViewSet, basename='nearMiss')

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:companyCode_slug>/', NearMissByCompanyViewSet.as_view({'get': 'list'}), name='nearMissByCompany'),
]