from rest_framework import serializers
from .models import SpareParts

from accounts.models import CompanyCode
from django.db.models import Max




class SparePartsSerializer(serializers.ModelSerializer):

    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )

    class Meta:
        model = SpareParts #呼び出すモデル名
        fields = ['companyCode','partsNo','image', 'bomCode', 'partsName', 'category', 'partsModel', 'serialNumber', 'taskCode', 'partsCost', 'numberOf', 'unit', 'location', 'partsDeliveryTime', 'orderAlert', 'orderSituation', 'classification', 'inventoryTurnover','partsDescription',]# API上に表示するモデルのデータ項目
    


class CompanyCodeSPSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, source='spareParts_companyCode')#ここのsourceは本当に注意
    
    def create(self, validated_data):
        spare_parts_data = validated_data.pop('spareParts_companyCode')
        company_code_data = validated_data.get('companyCode')

        company_code_instance, _ = CompanyCode.objects.get_or_create(companyCode=company_code_data, defaults=validated_data)

        for part_data in spare_parts_data:
            part_no = part_data.get('partsNo')
            part_instance = SpareParts.objects.filter(companyCode=company_code_instance, partsNo=part_no).first()
            
            if part_instance:
                # 既存のSparePartsを更新
                for key, value in part_data.items():
                    setattr(part_instance, key, value)
                part_instance.save()
            else:
                # 新規のSparePartsを追加
                SpareParts.objects.create(companyCode=company_code_instance, **part_data)

        return company_code_instance

    def update(self, instance, validated_data):
        spare_parts_data = validated_data.pop('spareParts_companyCode', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for part_data in spare_parts_data:
            part_no = part_data.get('partsNo')
            part_instance = SpareParts.objects.filter(companyCode=instance, partsNo=part_no).first()

            if part_instance:
                # 既存のSparePartsを更新
                for key, value in part_data.items():
                    setattr(part_instance, key, value)
                part_instance.save()
            else:
                # 新規のSparePartsを追加
                SpareParts.objects.create(companyCode=instance, **part_data)

        return instance

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']




