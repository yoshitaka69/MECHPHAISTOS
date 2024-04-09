from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (AlertScheduleViewSet,CompanyCodeAlertScheduleViewSet)


router = DefaultRouter()


router.register(r'alertSchedule', AlertScheduleViewSet, basename='alertSchedule')
router.register(r'alertScheduleByCompany', CompanyCodeAlertScheduleViewSet, basename='companyCode-alertSchedule')

urlpatterns = [
    path('agora/', include(router.urls)),
]