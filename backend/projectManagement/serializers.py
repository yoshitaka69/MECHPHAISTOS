from rest_framework import serializers
from .models import ProjectManagement
from accounts.models import CompanyCode

class ProjectManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManagement
        fields = '__all__'

    # ファイルアップロード処理
    def create(self, validated_data):
        return ProjectManagement.objects.create(**validated_data)
    
class CompanyCodePMSerializer(serializers.ModelSerializer):
    projectManagementList = ProjectManagementSerializer(many=True, read_only=True, source='projectManagement_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'projectManagementList']
