from rest_framework import viewsets

from accounts.models import CompanyCode
from .models import WorkOrder, WorkPermission, WorkOrderManagement
from .serializers import WorkOrderSerializer, CompanyCodeWorkOrderSerializer, WorkPermissionSerializer, CompanyCodeWorkPermissionSerializer, WorkOrderManagementSerializer, CompanyCodeWorkOrderManagementSerializer




class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class CompanyCodeWorkOrderViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkOrderSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('workOrder_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    



class WorkPermissionViewSet(viewsets.ModelViewSet):
    queryset = WorkPermission.objects.all()
    serializer_class = WorkPermissionSerializer

class CompanyCodeWorkPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkPermissionSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('workPermission_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




class WorkOrderManagementViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderManagement.objects.all()
    serializer_class = WorkOrderManagementSerializer

class CompanyCodeWorkOrderManagementViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkOrderManagementSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('workOrderManagement_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset