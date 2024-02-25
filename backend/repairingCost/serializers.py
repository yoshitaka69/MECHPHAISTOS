from rest_framework import serializers
from .models import Pm02,Pm03,Pm04,Pm05

class Pm02Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pm02 # 呼び出すモデル
        fields = [
            "plant",
            "plannedPM02",
            'plannedMonth',
            'plannedCost',
            'totalPlannedPM02',

            "actualPM02",
            'actualMonth',
            'actualCost',
            'totalActualPM02',

            'no1PlannedPM02',
            'no1ActualPM02'
        ] # API上に表示するモデルのデータ項目


class Pm03Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pm03 # 呼び出すモデル
        fields = [
            "plant",
            "plannedPM03",
            'plannedMonth',
            'plannedCost',
            'totalPlannedPM03',

            "actualPM03",
            'actualMonth',
            'actualCost',
            'totalActualPM03',

            'no1PlannedPM03',
            'no1ActualPM03'
        ] # API上に表示するモデルのデータ項目

class Pm04Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pm04 # 呼び出すモデル
        fields = [
            "plant",

            "actualPM04",
            'actualMonth',
            'actualCost',
            'totalActualPM04',

            'no1ActualPM04'
        ] # API上に表示するモデルのデータ項目

class Pm05Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pm05 # 呼び出すモデル
        fields = [
            "plant",
            "plannedPM05",
            'plannedMonth',
            'plannedCost',
            'totalPlannedPM05',

            "actualPM05",
            'actualMonth',
            'actualCost',
            'totalActualPM05',

            'no1PlannedPM05',
            'no1ActualPM05'
        ] # API上に表示するモデルのデータ項目