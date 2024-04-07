from django.shortcuts import render
from rest_framework import viewsets

from .models import MasterDataTable,BomAndTask,AlertSchedule
from accounts.models import CompanyCode
from .serializers import  (MasterDataTableSerializer, CompanyCodeMDTSerializer,
                        BomAndTaskSerializer,CompanyCodeBomAndTaskSerializer,
                        AlertScheduleSerializer,CompanyCodeAlertScheduleSerializer)


#MasterDataTable
class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer


class CompanyCodeMDTViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeMDTSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('masterDataTable_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



#BomAndTask
class BomAndTaskViewSet(viewsets.ModelViewSet):
    queryset = BomAndTask.objects.all()
    serializer_class = BomAndTaskSerializer


class CompanyCodeBomAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeBomAndTaskSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('bomAndTask_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



#AlertSchedule
class AlertScheduleViewSet(viewsets.ModelViewSet):
    queryset = AlertSchedule.objects.all()
    serializer_class = AlertScheduleSerializer


class CompanyCodeAlertScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAlertScheduleSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('alertSchedule_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
