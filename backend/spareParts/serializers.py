from rest_framework import serializers
from .models import SpareParts,BomList,SparePartsManagement

from accounts.models import CompanyCode,Plant
from django.db.models import Max




#------------------------------------------------------------
from rest_framework import serializers
from .models import SpareParts, CompanyCode, CompanyName, Plant, Equipment, Machine

from rest_framework import serializers
from .models import SpareParts, CompanyCode



class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = '__all__'

class CompanyCodeSPSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, read_only=True, source='spareParts_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']

    def create(self, validated_data):
        company_code_data = validated_data.pop('companyCode')
        instance = SpareParts.objects.create(companyCode=company_code_data, **validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.companyCode = validated_data.get('companyCode', instance.companyCode)
        instance.partsNo = validated_data.get('partsNo', instance.partsNo)
        instance.save()
        return instance






#------------------------------------------------------------





class BomListSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )
        
    class Meta:
        model = BomList #呼び出すモデル名
        fields = ['companyCode','bomCode','bomCost', 'maxPartsDeliveryTimeInBom',]

class CompanyBomListSerializer(serializers.ModelSerializer):
    bomList = BomListSerializer(many=True, source='bomList_companyCode')#ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'bomList']





from rest_framework import serializers
from .models import SparePartsManagement, CompanyCode

class SparePartsManagementSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )
    # plant フィールドを CharField として定義
    plant = serializers.CharField(max_length=200)

    class Meta:
        model = SparePartsManagement  # 呼び出すモデル名
        fields = ['companyCode', 'companyName', 'plant', 'equipment', 'machineName', 'totalSparePartsCost', 'inventoryTurnover']


class CompanySparePartsManagementSerializer(serializers.ModelSerializer):
    SparePartsManagementList = SparePartsManagementSerializer(many=True, source='sparePartsManagement_companyCode')  # ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'SparePartsManagementList']