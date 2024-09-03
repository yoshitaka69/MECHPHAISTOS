from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaintenanceWorkingReportViewSet, SpecsheetsCreateView

router = DefaultRouter()
router.register(r'maintenanceReports', MaintenanceWorkingReportViewSet, basename='maintenanceReport')

urlpatterns = [
    path('workingReport/', include(router.urls)),
    path('workingReport/specsheets/', SpecsheetsCreateView.as_view(), name='specsheets-create'),
]