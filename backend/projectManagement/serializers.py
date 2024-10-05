from rest_framework import serializers
from .models import ProjectManagement

class ProjectManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManagement
        fields = '__all__'

    # ファイルアップロード処理
    def create(self, validated_data):
        return ProjectManagement.objects.create(**validated_data)
