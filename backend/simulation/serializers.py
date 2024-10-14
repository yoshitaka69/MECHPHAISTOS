from rest_framework import serializers
from .models import No1Simulation, No2Simulation, No3Simulation
from accounts.models import CompanyCode



#------------------------------------------------------------------------
# No1Simulation用のシリアライザ
#------------------------------------------------------------------------
class No1SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = No1Simulation
        fields = '__all__'

# CompanyCode用のシリアライザにシミュレーションをネスト
class CompanyCodeNo1SimulationSerializer(serializers.ModelSerializer):
    no1SimulationList = No1SimulationSerializer(many=True, read_only=True, source='no1Simulation_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'no1SimulationList']
#------------------------------------------------------------------------



#------------------------------------------------------------------------
#No2Simulation用のシリアライザ
#------------------------------------------------------------------------
class No2SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = No2Simulation
        fields = '__all__'

class CompanyCodeNo2SimulationSerializer(serializers.ModelSerializer):
    no2SimulationList = No2SimulationSerializer(many=True, read_only=True, source='no2Simulation_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'no2SimulationList']
#------------------------------------------------------------------------


#------------------------------------------------------------------------
#No3Simulation用のシリアライザ
#------------------------------------------------------------------------
class No3SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = No3Simulation
        fields = '__all__'

class CompanyCodeNo3SimulationSerializer(serializers.ModelSerializer):
    no3SimulationList = No3SimulationSerializer(many=True, read_only=True, source='no3Simulation_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'no3SimulationList']
#------------------------------------------------------------------------