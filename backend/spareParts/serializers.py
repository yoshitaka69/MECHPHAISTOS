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
        
        # 既存のSparePartsのpartsNoを取得
        existing_parts_nos = set(instance.spareParts_companyCode.values_list('partsNo', flat=True))

        for part_data in spare_parts_data:
            parts_no = part_data.get('partsNo')

            if parts_no in existing_parts_nos:
                # 既存のSparePartsインスタンスを更新
                spare_part_instance = instance.spareParts_companyCode.get(partsNo=parts_no)
                for key, value in part_data.items():
                    setattr(spare_part_instance, key, value)
                spare_part_instance.save()
            else:
                # 新しいSparePartsインスタンスを追加
                SpareParts.objects.create(companyCode=instance, **part_data)

        return instance

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']




