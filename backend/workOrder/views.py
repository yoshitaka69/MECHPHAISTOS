from rest_framework import viewsets

from accounts.models import CompanyCode
from .models import WorkOrder, WorkPermission, WorkOrderManagement
from .serializers import WorkOrderSerializer, CompanyCodeWorkOrderSerializer, WorkPermissionSerializer, CompanyCodeWorkPermissionSerializer, WorkOrderManagementSerializer, CompanyCodeWorkOrderManagementSerializer




class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

class CompanyCodeWorkOrderViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkOrderSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('workOrder_companyCode').all()
    



class WorkPermissionViewSet(viewsets.ModelViewSet):
    queryset = WorkPermission.objects.all()
    serializer_class = WorkPermissionSerializer

class CompanyCodeWorkPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkPermissionSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('workPermission_companyCode').all()




class WorkOrderManagementViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderManagement.objects.all()
    serializer_class = WorkOrderManagementSerializer

class CompanyCodeWorkOrderManagementViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkOrderManagementSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('workOrderManagement_companyCode').all()