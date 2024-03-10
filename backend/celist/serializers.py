from rest_framework import serializers
from .models import CeList,CompanyCode,Plant,Equipment,Machine

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment 
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine 
        fields = '__all__'

class CeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CeList
        fields = '__all__'

class CompanyCodeCeSerializer(serializers.ModelSerializer):
    ceList = CeSerializer(many=True, read_only=True, source='ce_set')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ceList']

