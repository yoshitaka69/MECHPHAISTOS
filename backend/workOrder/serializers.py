from rest_framework import serializers
from .models import WorkOrder, WorkPermission, WorkOrderManagement
from accounts.models import CompanyCode






#---------------------------------------------------------------------------------------------------------------
from rest_framework import serializers
from .models import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'
        read_only_fields = ('workOrderNo',)  # workOrderNoを読み取り専用に設定


class CompanyCodeWorkOrderSerializer(serializers.ModelSerializer):
    workOrderList = WorkOrderSerializer(many=True, read_only=True, source='workOrder_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'workOrderList']



#---------------------------------------------------------------------------------------------------------------
        
















#---------------------------------------------------------------------------------------------------------------

class WorkPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPermission
        fields = '__all__'

class CompanyCodeWorkPermissionSerializer(serializers.ModelSerializer):
    workOrderPermissionList = WorkPermissionSerializer(many=True, read_only=True, source='workOrderMission_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'workOrderPermissionList']




class WorkOrderManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrderManagement
        fields = ['companyCode','companyName','plant', 'equipment',]

class CompanyCodeWorkOrderManagementSerializer(serializers.ModelSerializer):
    WorkOrderManagement = WorkOrderManagementSerializer(many=True, read_only=True, source='workOrderManagement_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'WorkOrderManagement']





#---------------------------------------------------------------------------------------------------------------

from rest_framework import serializers
from .models import DailyReport, CompanyCode

class DailyReportSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCodeフィールドをキーに使用
        queryset=CompanyCode.objects.all()  # バリデーション用のクエリセット
    )

    class Meta:
        model = DailyReport
        fields = '__all__'


class CompanyCodeWithReportsSerializer(serializers.ModelSerializer):
    dailyReports = DailyReportSerializer(many=True, read_only=True, source='dailyReport_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'dailyReports']