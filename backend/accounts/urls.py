from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet,CustomUserViewSet#,PaymentViewSet

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

router = DefaultRouter()
router.register(r'customUser', CustomUserViewSet, basename='customUser')
router.register(r'company', CompanyViewSet, basename='company')
#router.register(r'payment', PaymentViewSet, basename='payments')

urlpatterns = [
    path('accounts/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]