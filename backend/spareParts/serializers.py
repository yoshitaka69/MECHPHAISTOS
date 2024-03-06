from rest_framework import serializers
from .models import SpareParts,Company


class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目

class CompanySparePartsSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, read_only=True, source='spareParts_set')

    class Meta:
        model = Company
        fields = ['companyCode', 'sparePartsList']

