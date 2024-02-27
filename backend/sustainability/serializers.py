from rest_framework import serializers
from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas


#ネストしたCo2シリアライザー
class Co2DataSerializer(serializers.Serializer):
    date = serializers.DateField()
    co2Cost = serializers.FloatField()
class Co2Serializer(serializers.ModelSerializer):
    co2_data = Co2DataSerializer(source='*')

    class Meta:
        model = Co2# 呼び出すモデル
        fields = [
            "plant",
            "co2_data",
            'createdDay',
            'updateDay',
        ]# API上に表示するモデルのデータ項目
        depth:1


class StmDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    stmCost = serializers.FloatField()
class StmSerializer(serializers.ModelSerializer):
    stm_data = StmDataSerializer(source='*')

    class Meta:
        model = Stm  # 呼び出すモデル
        fields = [
            "plant",
            "stm_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 1  # 深さの指定


class ElectricityUsageDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    elecCost = serializers.FloatField()
class ElectricityUsageSerializer(serializers.ModelSerializer):
    elec_usage_data = ElectricityUsageDataSerializer(source='*')

    class Meta:
        model = ElectricityUsage  # 呼び出すモデル
        fields = [
            "plant",
            "elec_usage_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目


class CompressedAirDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    compAirCost = serializers.FloatField()
class CompressedAirSerializer(serializers.ModelSerializer):
    comp_air_data = CompressedAirDataSerializer(source='*')
    class Meta:
        model = CompressedAir  # 呼び出すモデル
        fields = [
            "plant",
            "comp_air_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目



class WellWaterDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    wellWaterCost = serializers.FloatField()
class WellWaterSerializer(serializers.ModelSerializer):
    well_water_data = WellWaterDataSerializer(source='*')

    class Meta:
        model = WellWater  # 呼び出すモデル
        fields = [
            "plant",
            "well_water_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目



class PureWaterDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    pureWaterCost = serializers.FloatField()

class PureWaterSerializer(serializers.ModelSerializer):
    pure_water_data = PureWaterDataSerializer(source='*')

    class Meta:
        model = PureWater  # 呼び出すモデル
        fields = [
            "plant",
            "pure_water_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目



class WwtDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    wwtCost = serializers.FloatField()

class WwtSerializer(serializers.ModelSerializer):
    wwt_data = WwtDataSerializer(source='*')

    class Meta:
        model = Wwt  # 呼び出すモデル
        fields = [
            "plant",
            "wwt_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目



class ExhaustGasDataSerializer(serializers.Serializer):
    date = serializers.DateField()
class ExhaustGasSerializer(serializers.ModelSerializer):
    exhaust_gas_data = ExhaustGasDataSerializer(source='*')

    class Meta:
        model = ExhaustGas  # 呼び出すモデル
        fields = [
            "plant",
            "exhaust_gas_data",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
