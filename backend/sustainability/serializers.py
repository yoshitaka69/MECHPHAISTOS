from rest_framework import serializers
from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas
from accounts.models import CompanyCode


class Co2Serializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Co2
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'co2Cost', 'createdDay', 'updateDay']

class CompanyCodeCo2Serializer(serializers.ModelSerializer):
    co2List = Co2Serializer(many=True, read_only=True, source='co2_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'co2List']




class StmSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Stm
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'stmCost', 'createdDay', 'updateDay']

class CompanyCodeStmSerializer(serializers.ModelSerializer):
    stmList = StmSerializer(many=True, read_only=True, source='stm_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'stmList']




class ElectricityUsageSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = ElectricityUsage
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'elecCost', 'createdDay', 'updateDay']

class CompanyCodeElectricityUsageSerializer(serializers.ModelSerializer):
    elecList = ElectricityUsageSerializer(many=True, read_only=True, source='elec_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'elecList']





class CompressedAirSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = CompressedAir
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'compAirCost', 'createdDay', 'updateDay']

class CompanyCodeCompressedAirSerializer(serializers.ModelSerializer):
    compAirList = CompressedAirSerializer(many=True, read_only=True, source='compAir_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'compAirList']




class WellWaterSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = WellWater
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'wellWaterCost', 'createdDay', 'updateDay']

class CompanyCodeWellWaterSerializer(serializers.ModelSerializer):
    wellWaterList = WellWaterSerializer(many=True, read_only=True, source='wellWater_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'wellWaterList']



class PureWaterSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = PureWater
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'pureWaterCost', 'createdDay', 'updateDay']

class CompanyCodePureWaterSerializer(serializers.ModelSerializer):
    pureWaterList = PureWaterSerializer(many=True, read_only=True, source='pureWater_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'pureWaterList']




class WwtSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Wwt
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'wwtCost', 'createdDay', 'updateDay']

class CompanyCodeWwtSerializer(serializers.ModelSerializer):
    wwtList = WwtSerializer(many=True, read_only=True, source='wwt_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'wwtList']



class WwtSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = Wwt
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'wwtCost', 'createdDay', 'updateDay']

class CompanyCodeWwtSerializer(serializers.ModelSerializer):
    wwtList = WwtSerializer(many=True, read_only=True, source='wwt_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'wwtList']




class ExhaustGasSerializer(serializers.ModelSerializer):
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = ExhaustGas
        fields = ['id', 'companyCode', 'companyName', 'plant', 'date', 'exhaustGasCost', 'createdDay', 'updateDay']

class CompanyCodeExhaustGasSerializer(serializers.ModelSerializer):
    exhaustGasList = ExhaustGasSerializer(many=True, read_only=True, source='exhaustGas_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った…。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'exhaustGasList']

