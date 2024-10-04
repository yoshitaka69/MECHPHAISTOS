from rest_framework import viewsets, status  # 必要なモジュールを一度にインポート
from rest_framework.response import Response
from django.db.models import Max

from accounts.models import CompanyCode  # CompanyCodeのモデルインポート
from .models import WorkOrder, WorkPermission, WorkOrderManagement  # 使用する全てのモデルをまとめてインポート
from .serializers import (  # シリアライザーもまとめてインポート
    WorkOrderSerializer, 
    CompanyCodeWorkOrderSerializer, 
    WorkPermissionSerializer, 
    CompanyCodeWorkPermissionSerializer, 
    WorkOrderManagementSerializer, 
    CompanyCodeWorkOrderManagementSerializer
)



#--------------------------------------------------------------



class WorkOrderViewSet(viewsets.ModelViewSet):
    # WorkOrderモデルの全てのインスタンスを対象にしたクエリセットを設定
    queryset = WorkOrder.objects.all()
    # シリアライザとしてWorkOrderSerializerを使用
    serializer_class = WorkOrderSerializer

    # POSTリクエスト時の処理 (新規作成または更新)
    def create(self, request, *args, **kwargs):
        # リクエストデータを取得
        data = request.data
        print(f"Received data: {data}")

        # companyCodeとworkOrderNoを取得
        company_code_str = data.get('companyCode')
        work_order_no = data.get('workOrderNo')

        # companyCodeまたはworkOrderNoが存在しない場合はエラーレスポンスを返す
        if not company_code_str or not work_order_no:
            return Response(
                {"error": "companyCode and workOrderNo are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        print(f"Received companyCode: {company_code_str}, workOrderNo: {work_order_no}")

        # companyCodeをCompanyCodeオブジェクトに変換し、データに設定
        try:
            company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
            data['companyCode'] = company_code_obj.id
            print(f"Converted companyCode to ID: {data['companyCode']}")
        except CompanyCode.DoesNotExist:
            # companyCodeが存在しない場合はエラーレスポンスを返す
            return Response(
                {"error": f"CompanyCode '{company_code_str}' does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # companyCodeとworkOrderNoでWorkOrderの存在を確認
        try:
            existing_work_order = WorkOrder.objects.get(companyCode=company_code_obj, workOrderNo=work_order_no)
            print(f"Work order found: {existing_work_order}")

            # 既存のWorkOrderが存在する場合、更新処理を行う
            serializer = self.get_serializer(existing_work_order, data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            # 更新が成功したことを返す
            return Response({
                "workOrderNo": existing_work_order.workOrderNo,
                "message": "Work order updated successfully."
            }, status=status.HTTP_200_OK)

        except WorkOrder.DoesNotExist:
            # WorkOrderが存在しない場合、新規作成を行う
            print("No existing work order found. Creating a new one.")

            # シリアライザにデータを渡し、バリデーションを実行
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # 作成が成功したことを返す
            return Response({
                "workOrderNo": serializer.data['workOrderNo'],
                "message": "Work order created successfully."
            }, status=status.HTTP_201_CREATED)

    # perform_createメソッドで新規作成の保存処理を実行
    def perform_create(self, serializer):
        try:
            # WorkOrderインスタンスを保存
            work_order = serializer.save()
            print(f"Successfully created work order: {work_order}")
            return work_order
        except Exception as e:
            # エラー発生時の処理
            print(f"Error during serializer.save(): {e}")
            raise e

    # perform_updateメソッドで更新処理を実行
    def perform_update(self, serializer):
        try:
            # WorkOrderインスタンスを更新
            work_order = serializer.save()
            print(f"Successfully updated work order: {work_order}")
            return work_order
        except Exception as e:
            # エラー発生時の処理
            print(f"Error during serializer.save(): {e}")
            raise e

    # PUT/PATCHリクエスト時の更新処理
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # PATCHリクエストなら部分更新
        instance = self.get_object()  # 対象のWorkOrderインスタンスを取得
        data = request.data

        # companyCodeがリクエストデータに含まれている場合は変換する
        company_code_str = data.get('companyCode')
        if company_code_str:
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                data['companyCode'] = company_code_obj.id
            except CompanyCode.DoesNotExist:
                # companyCodeが存在しない場合はエラーレスポンスを返す
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # シリアライザでバリデーションを行い、更新処理を実行
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # 更新成功後のレスポンスを返す
        return Response(serializer.data)

    # 更新処理を行うperform_updateメソッド
    def perform_update(self, serializer):
        # データを保存 (更新)
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
