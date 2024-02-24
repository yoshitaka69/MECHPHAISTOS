from rest_framework import serializers
from .models import Co2List,StmList,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas


class Co2ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Co2List # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'co2Cost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目

class StmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StmList # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'stmCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目

class ElectricityUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricityUsage # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'elecCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目


class CompressedAirSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompressedAir # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'compAirCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目


class WellWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WellWater # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'wellWaterCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目


class PureWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PureWater # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'pureWaterCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目


class WwtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wwt # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'wwtCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目


class ExhaustGasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhaustGas # 呼び出すモデル
        fields = [
            "plant",
            "date",
            'ExhaustGasCost',
            'createdDay',
            'updateDay',
        ] # API上に表示するモデルのデータ項目