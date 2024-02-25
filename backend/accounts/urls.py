from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet,UserViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'user', UserViewSet, basename='user')
router.register(r'payment', PaymentViewSet, basename='payments')

urlpatterns = [
    path('accounts/', include(router.urls)),
]