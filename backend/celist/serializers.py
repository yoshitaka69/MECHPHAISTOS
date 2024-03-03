from rest_framework import serializers
from .models import Ce,SpareParts,Task


class CeSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = Ce # 呼び出すモデル
        fields = [
            "ceListNo",
            "companyCode",#one to one Field
            "plant",#one to one Field
            "locationNo",
            "function",
            "equipment",
            "bomNo",#one to one Field
            "totalBomCost",

            "valueImpact",
            "constructionPeriod",
            "partsDeliveryTime",
            "mttr",

            "countOfPM02",
            "latestPM02",
            "taskOfPM02",

            "countOfPM03",
            "latestPM03",
            "taskOfPM03",

            "countOfPM04",
            "latestPM04",
            "taskOfPM04",

            "countOfPM05",
            "latestPM05",
            "taskOfPM05",
            
            'nextEventDate',
            'situation',
            'ceDescription',
        ] # API上に表示するモデルのデータ項目

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