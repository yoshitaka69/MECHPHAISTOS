from rest_framework import serializers
from .models import Ce,Company


class CeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ce #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目

class CompanyCeSerializer(serializers.ModelSerializer):
    ceList = CeSerializer(many=True, read_only=True, source='ce_set')

    class Meta:
        model = Company
        fields = ['companyCode', 'ceList']

