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

    # POSTリクエスト時の処理 (作成)
    def create(self, request, *args, **kwargs):
        data = request.data
        print(f"Received data: {data}")

        company_code_str = data.get('companyCode')
        print(f"Received companyCode: {company_code_str}")

        if company_code_str:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                data['companyCode'] = company_code_obj.id
                print(f"Converted companyCode to ID: {data['companyCode']}")
            except CompanyCode.DoesNotExist:
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # perform_createを通してWorkOrderインスタンスを作成
        work_order = self.perform_create(serializer)

        if work_order is None:
            return Response(
                {"error": "Work order could not be created."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        print(f"Work order created with No: {work_order.workOrderNo}")

        return Response({
            "workOrderNo": work_order.workOrderNo,
            "message": "Work order created successfully."
        }, status=status.HTTP_201_CREATED)

    # perform_createメソッドで保存処理
    def perform_create(self, serializer):
        try:
            # WorkOrderインスタンスを保存
            work_order = serializer.save()
            print(f"Successfully created work order: {work_order}")
            return work_order
        except Exception as e:
            print(f"Error during serializer.save(): {e}")
            raise e

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data

        company_code_str = data.get('companyCode')
        if company_code_str:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                data['companyCode'] = company_code_obj.id
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

    # クエリパラメータに基づいて、companyCodeでフィルタリングされた作業指示を取得
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('workOrder_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    


#--------------------------------------------------------------


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import WorkPermission, CompanyCode
from .serializers import WorkPermissionSerializer

class WorkPermissionViewSet(viewsets.ModelViewSet):
    queryset = WorkPermission.objects.all()
    serializer_class = WorkPermissionSerializer

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


class CompanyCodeWorkPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWorkPermissionSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('workPermission_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



#--------------------------------------------------------------




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
    


#--------------------------------------------------------------


from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.files.base import ContentFile
import base64
from .models import DailyReport, CompanyCode
from .serializers import DailyReportSerializer, CompanyCodeWithReportsSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import DailyReport, CompanyCode
from .serializers import DailyReportSerializer

class DailyReportViewSet(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # デバッグ用: companyCodeの値を表示
        print("companyCode received:", data.get('companyCode'))

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyCodeViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeWithReportsSerializer  # シリアライザーを指定

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('dailyReport_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
