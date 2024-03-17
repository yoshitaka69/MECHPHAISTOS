from rest_framework import serializers
from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas
from accounts.models import CompanyCode,Plant


#Co2
class Co2Serializer(serializers.ModelSerializer):
    co2 = serializers.DecimalField(max_digits=15, decimal_places=5, source='co2Cost') 

    class Meta:
        model = Co2
        fields = ['date', 'co2']

class PlantCo2Serializer(serializers.ModelSerializer):
    Co2 = Co2Serializer(many=True, source='co2_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'Co2']

class CompanyCodeCo2Serializer(serializers.ModelSerializer):
    Co2List = PlantCo2Serializer(many=True, source='plant_companyCode')  # Plant モデルの related_name

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'Co2List']






#STM
class StmSerializer(serializers.ModelSerializer):
    stm = serializers.DecimalField(max_digits=15, decimal_places=5, source='stmCost') 

    class Meta:
        model = Stm
        fields = ['date', 'stm']

class PlantStmSerializer(serializers.ModelSerializer):
    Stm = StmSerializer(many=True, source='stm_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'Stm']

class CompanyCodeStmSerializer(serializers.ModelSerializer):
    StmList = PlantStmSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'StmList']





#elec
class ElecSerializer(serializers.ModelSerializer):
    elec = serializers.DecimalField(max_digits=15, decimal_places=5, source='elecCost') 

    class Meta:
        model = ElectricityUsage
        fields = ['date', 'elec']

class PlantElecSerializer(serializers.ModelSerializer):
    Elec = ElecSerializer(many=True, source='elec_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'Elec']

class CompanyCodeElecSerializer(serializers.ModelSerializer):
    ElecList = PlantElecSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ElecList']








#CompAir
class CompAirSerializer(serializers.ModelSerializer):
    compAir = serializers.DecimalField(max_digits=15, decimal_places=5, source='compAirCost') 

    class Meta:
        model = CompressedAir
        fields = ['date', 'compAir']

class PlantCompAirSerializer(serializers.ModelSerializer):
    CompAir = CompAirSerializer(many=True, source='compAir_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'CompAir']

class CompanyCodeCompAirSerializer(serializers.ModelSerializer):
    CompAirList = PlantCompAirSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'CompAirList']




#WellWater
class WellWaterSerializer(serializers.ModelSerializer):
    wellWater = serializers.DecimalField(max_digits=15, decimal_places=5, source='wellWaterCost') 

    class Meta:
        model = WellWater
        fields = ['date', 'wellWater']

class PlantWellWaterSerializer(serializers.ModelSerializer):
    WellWater = WellWaterSerializer(many=True, source='wellWater_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'WellWater']

class CompanyCodeWellWaterSerializer(serializers.ModelSerializer):
    WellWaterList = PlantWellWaterSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'WellWaterList']






#PureWater
class PureWaterSerializer(serializers.ModelSerializer):
    pureWater = serializers.DecimalField(max_digits=15, decimal_places=5, source='pureWaterCost') 

    class Meta:
        model = PureWater
        fields = ['date', 'pureWater']

class PlantPureWaterSerializer(serializers.ModelSerializer):
    PureWater = PureWaterSerializer(many=True, source='pureWater_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'PureWater']

class CompanyCodePureWaterSerializer(serializers.ModelSerializer):
    PureWaterList = PlantPureWaterSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'PureWaterList']







#Wwt
class WwtSerializer(serializers.ModelSerializer):
    wwt = serializers.DecimalField(max_digits=15, decimal_places=5, source='wwtCost') 

    class Meta:
        model = Wwt
        fields = ['date', 'wwt']

class PlantWwtSerializer(serializers.ModelSerializer):
    Wwt = WwtSerializer(many=True, source='wwt_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'Wwt']

class CompanyCodeWwtSerializer(serializers.ModelSerializer):
    WwtList = PlantWwtSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'WwtList']






#ExhaustGas
class ExhaustGasSerializer(serializers.ModelSerializer):
    exhaustGas = serializers.DecimalField(max_digits=15, decimal_places=5, source='exhaustGasCost') 

    class Meta:
        model = ExhaustGas
        fields = ['date', 'exhaustGas']

class PlantExhaustGasSerializer(serializers.ModelSerializer):
    ExhaustGas = ExhaustGasSerializer(many=True, source='exhaustGas_plant')  

    class Meta:
        model = Plant
        fields = ['plant', 'ExhaustGas']

class CompanyCodeExhaustGasSerializer(serializers.ModelSerializer):
    ExhaustGasList = PlantExhaustGasSerializer(many=True, source='plant_companyCode') 

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ExhaustGasList']
