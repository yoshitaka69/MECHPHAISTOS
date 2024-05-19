from rest_framework import serializers
from .models import WorkOrder, WorkPermission, WorkOrderManagement
from accounts.models import CompanyCode



class WorkOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrder
        fields = ['companyCode','companyName','plant', 'equipment', 'workOrderNo','workOrderDesc','status']

class CompanyCodeWorkOrderSerializer(serializers.ModelSerializer):
    workOrderList = WorkOrderSerializer(many=True, read_only=True, source='workOrder_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'workOrderList']
        



class WorkPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkPermission
        fields = ['companyCode','companyName','plant', 'equipment', 'workOrderNo', 'workPermissionNo', 'workPermissionDesc','status']

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