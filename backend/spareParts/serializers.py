from rest_framework import serializers
from .models import SpareParts

from accounts.models import CompanyCode
from django.db.models import Max




class SparePartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpareParts #呼び出すモデル名
        fields = ['image', 'bomCode', 'partsName', 'category', 'partsModel', 'serialNumber', 'taskCode', 'partsCost', 'numberOf', 'unit', 'location', 'partsDeliveryTime', 'orderAlert', 'orderSituation', 'classification', 'inventoryTurnover',]# API上に表示するモデルのデータ項目


class CompanyCodeSPSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, source='spareParts_companyCode')#ここのsourceは本当に注意
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']

