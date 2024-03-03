from rest_framework import serializers
from .models import Pm02,Pm03,Pm04,Pm05

from accounts.models import Company
from accounts.serializers import CompanySerializer

from ceList.models import Ce
from ceList.serializers import CeSerializer


class RCCompanyCodeSerializer(serializers.ModelSerializer):
    companyCode = CompanySerializer(read_only=True)
    class Meta:
        model = Company
        fields = ["companyCode"]

class RCPlantSerializer(serializers.ModelSerializer):
    companyCode = RCCompanyCodeSerializer(read_only=True)
    ce = CeSerializer(read_only=True)

    class Meta:
        model = Ce
        fields = ["companyCode","plant"]


class Pm02Serializer(serializers.ModelSerializer):

    companyCode = RCCompanyCodeSerializer(read_only=True)
    plant = RCPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Pm02 # 呼び出すモデル
        fields = [
            "companyCode",
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

    companyCode = RCCompanyCodeSerializer(read_only=True)
    plant = RCPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Pm03 # 呼び出すモデル
        fields = [
            "companyCode",
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

    companyCode = RCCompanyCodeSerializer(read_only=True)
    plant = RCPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Pm04 # 呼び出すモデル
        fields = [
            "companyCode",
            "plant",

            "actualPM04",
            'actualMonth',
            'actualCost',
            'totalActualPM04',

            'no1ActualPM04'
        ] # API上に表示するモデルのデータ項目

class Pm05Serializer(serializers.ModelSerializer):

    companyCode = RCCompanyCodeSerializer(read_only=True)
    plant = RCPlantSerializer(read_only=True)
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Pm05 # 呼び出すモデル
        fields = [
            "companyCode",
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