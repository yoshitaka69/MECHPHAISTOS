from rest_framework import serializers
from .models import Ce,SpareParts,Task,Company


class CeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ce #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目

class CompanyCeSerializer(serializers.ModelSerializer):
    ceList = CeSerializer(many=True, read_only=True, source='ce_set')

    class Meta:
        model = Company
        fields = ['companyCode', 'ceList']



class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts # 呼び出すモデル
        fields = [
            "image",
            "partsName",
            "category",
            "partsModel",
            "serialNumber",
            "taskListNo",
            "partsCost",
            "numberOf",
            "unit",
            "location",
            "partsDeliveryTime",
            "partsDescription",
        ] # API上に表示するモデルのデータ項目

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task # 呼び出すモデル
        fields = [
            "plant",
            "equipment",
            "function",
            "latestPM02",
            "latestPM03",
            "latestPM04",
            "taskOfPM02",
            "laborCost",
            "partsName",
            "constructionPeriod",
            "nextEventDate",
            "situation",
            'thisYear10ago',
            'thisYear9ago',
            'thisYear8ago',
            'thisYear7ago',
            'thisYear6ago',
            'thisYear5ago',
            'thisYear4ago',
            'thisYear3ago',
            'thisYear2ago',
            'thisYear1ago',
            'thisYear',
            'thisYear1later',
            'thisYear2later',
            'thisYear3later',
            'thisYear4later',
            'thisYear5later',
            'thisYear6later',
            'thisYear7later',
            'thisYear8later',
            'thisYear9later',
            'thisYear10later',
        ] # API上に表示するモデルのデータ項目