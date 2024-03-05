from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NearMissViewSet, company_near_miss_list, NearMissByCompanyViewSet

# ルーターの設定
router = DefaultRouter()
router.register(r'nearmiss', NearMissViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company-near-misses/', company_near_miss_list, name='company-near-misses'),
    path('nearmiss-by-company/<str:companyCode_slug>/', NearMissByCompanyViewSet.as_view({'get': 'list'}), name='nearmiss-by-company')
]
