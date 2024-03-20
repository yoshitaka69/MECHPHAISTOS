from rest_framework import serializers
from .models import SpareParts
from accounts.models import CompanyCode

from django.db.models import Max


class SparePartsSerializer(serializers.ModelSerializer):
    bomCode = serializers.SerializerMethodField()
    class Meta:
        model = SpareParts #呼び出すモデル名
        fields = '__all__'# API上に表示するモデルのデータ項目

    def get_custom_id(self, obj):
        # companyCode を基に最大のカスタム ID を検索
        last_id = SpareParts.objects.filter(companyCode=obj.companyCode).aggregate(Max('bomCode_id'))['bomCode_id__max']

        # 新しいカスタム ID を生成（最初の場合は 1 から開始）
        new_id = 1 if last_id is None else last_id + 1

        return f"{obj.companyCode}-{new_id}"
    
    def create(self, validated_data):
        # カスタム ID を計算（例として 'companyCode' がモデル内に存在すると仮定）
        company_code = validated_data['companyCode']
        last_id = SpareParts.objects.filter(companyCode=company_code).aggregate(Max('bomCode_id'))['bomCode_id__max']
        new_id = 1 if last_id is None else last_id + 1

        # 新しいインスタンスを生成して保存
        instance = SpareParts(**validated_data, custom_id=new_id)
        instance.save()
        return instance


class CompanyCodeSPSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, read_only=True, source='spareParts_companyCode')#ここのsourceは本当に注意
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']

