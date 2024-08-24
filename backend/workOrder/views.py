from rest_framework import viewsets

from accounts.models import CompanyCode
from .models import WorkOrder, WorkPermission, WorkOrderManagement
from .serializers import WorkOrderSerializer, CompanyCodeWorkOrderSerializer, WorkPermissionSerializer, CompanyCodeWorkPermissionSerializer, WorkOrderManagementSerializer, CompanyCodeWorkOrderManagementSerializer





#--------------------------------------------------------------


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import WorkOrder, CompanyCode
from .serializers import WorkOrderSerializer
from django.db.models import Max

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        # companyCodeが文字列として渡された場合、それに対応するオブジェクトを取得
        company_code_str = data.get('companyCode')
        if company_code_str:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                data['companyCode'] = company_code_obj.id  # IDに変換
            except CompanyCode.DoesNotExist:
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data

        # companyCodeが文字列として渡された場合、それに対応するオブジェクトを取得
        company_code_str = data.get('companyCode')
        if company_code_str:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                data['companyCode'] = company_code_obj.id  # IDに変換
            except CompanyCode.DoesNotExist:
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()





class CompanyCodeWorkOrderViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkOrderSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('workOrder_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    


#--------------------------------------------------------------














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