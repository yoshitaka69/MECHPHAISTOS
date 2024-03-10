from rest_framework import serializers
from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas

from accounts.models import Company
from accounts.serializers import CompanySerializer

from ceList.models import Plant
from ceList.serializers import PlantSerializer



class EnPICompanyCodeSerializer(serializers.ModelSerializer):
    companyCode = CompanySerializer(read_only=True)
    class Meta:
        model = Company
        fields = ["companyCode"]

class EnPIPlantSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = PlantSerializer(read_only=True)

    class Meta:
        model = Plant
        fields = ["companyCode","plant"]


class Co2Serializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Co2# 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "co2Cost",
            'createdDay',
            'updateDay',
        ]# API上に表示するモデルのデータ項目
        depth = 2


class StmSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = Stm  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "stmCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定

class ElectricityUsageSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = ElectricityUsage  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "elecCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定


class CompressedAirSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = CompressedAir  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "compAirCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定

class WellWaterSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = WellWater  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "wellWaterCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定


class PureWaterSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = PureWater  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "pureWaterCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定

class WwtSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 

    class Meta:
        model = Wwt  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "wwtCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定

class ExhaustGasSerializer(serializers.ModelSerializer):
    companyCode = EnPICompanyCodeSerializer(read_only=True)
    plant = EnPIPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    
    class Meta:
        model = ExhaustGas  # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",
            "date",
            "exhaustGasCost",
            'createdDay',
            'updateDay',
        ]  # API上に表示するモデルのデータ項目
        depth = 3 # 深さの指定