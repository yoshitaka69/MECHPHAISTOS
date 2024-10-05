from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectManagementViewSet,CompanyCodePMViewSet

router = DefaultRouter()
router.register(r'projectManagement', ProjectManagementViewSet, basename='projectManagement')
router.register(r'projectManagementByCompany', CompanyCodePMViewSet, basename='companyCode-projectManagement')

urlpatterns = [
    path('projectManagement/', include(router.urls)),
]
