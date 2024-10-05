from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectManagementViewSet

router = DefaultRouter()
router.register(r'projectManagement', ProjectManagementViewSet)

urlpatterns = [
    path('projectManagement/', include(router.urls)),
]
