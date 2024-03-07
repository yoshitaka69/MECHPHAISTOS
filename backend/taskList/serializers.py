from rest_framework import serializers
from .models import Task,Company


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目

class CompanyTaskSerializer(serializers.ModelSerializer):
    taskList = TaskSerializer(many=True, read_only=True, source='task_set')

    class Meta:
        model = Company
        fields = ['companyCode', 'taskList']

