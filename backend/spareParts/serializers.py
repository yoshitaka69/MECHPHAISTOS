from rest_framework import serializers
from .models import SpareParts,BomList,SparePartsManagement

from accounts.models import CompanyCode
from django.db.models import Max




class SparePartsSerializer(serializers.ModelSerializer):

    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )

    class Meta:
        model = SpareParts #呼び出すモデル名
        fields = ['companyCode','partsNo','image', 'bomCode', 'partsName', 'category', 'partsModel', 'serialNumber', 'taskCode', 'partsCost', 'numberOf', 'summedPartsCost','unit', 'location', 'partsDeliveryTime', 'orderAlert', 'orderSituation', 'classification', 'inventoryTurnover','partsDescription',]# API上に表示するモデルのデータ項目


class CompanyCodeSPSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, source='spareParts_companyCode')#ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']






class BomListSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )
        
    class Meta:
        model = BomList #呼び出すモデル名
        fields = ['companyCode','bomCode','bomCost', 'maxPartsDeliveryTimeInBom',]

class CompanyBomListSerializer(serializers.ModelSerializer):
    bomList = BomListSerializer(many=True, source='bomList_companyCode')#ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        field = ['companyCode', 'bomList']





class SparePartsManagementSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )
    class Meta:
        model = SparePartsManagement #呼び出すモデル名
        fields = ['companyCode','companyName','plant', 'equipment','machineName','totalSparePartsCost']


class CompanySparePartsManagementSerializer(serializers.ModelSerializer):
    SparePartsManagementList = SparePartsManagementSerializer(many=True, source='sparePartsManagement_companyCode')#ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        field = ['companyCode', 'SparePartsManagementList']