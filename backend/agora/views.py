from django.shortcuts import render
from rest_framework import viewsets

from .models import AlertSchedule
from accounts.models import CompanyCode
from .serializers import  AlertScheduleSerializer,CompanyCodeAlertScheduleSerializer



#AlertSchedule
class AlertScheduleViewSet(viewsets.ModelViewSet):
    queryset = AlertSchedule.objects.all()
    serializer_class = AlertScheduleSerializer

class CompanyCodeAlertScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAlertScheduleSerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('alertSchedule_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset