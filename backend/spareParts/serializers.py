from rest_framework import serializers
from .models import SpareParts,BomList,SparePartsManagement

from accounts.models import CompanyCode,Plant
from django.db.models import Max




#------------------------------------------------------------
from rest_framework import serializers
from .models import SpareParts, CompanyCode, CompanyName, Plant, Equipment, Machine

class SparePartsSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',
        queryset=CompanyCode.objects.all()
    )
    companyName = serializers.SlugRelatedField(
        slug_field='companyName',
        queryset=CompanyName.objects.all(),
        allow_null=True,
        required=False
    )
    plant = serializers.SlugRelatedField(
        slug_field='plantName',
        queryset=Plant.objects.all(),
        allow_null=True,
        required=False
    )
    equipment = serializers.SlugRelatedField(
        slug_field='equipmentName',
        queryset=Equipment.objects.all(),
        allow_null=True,
        required=False
    )
    machineName = serializers.SlugRelatedField(
        slug_field='machineName',
        queryset=Machine.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = SpareParts
        fields = [
            'companyCode',
            'companyName',
            'plant',
            'equipment',
            'machineName',
            'partsNo',
            'image',
            'bomCode',
            'partsName',
            'category',
            'partsModel',
            'serialNumber',
            'partsCost',
            'numberOf',
            'summedPartsCost',
            'unit',
            'taskCode',
            'location',
            'stock',
            'partsDeliveryTime',
            'orderAlert',
            'orderSituation',
            'classification',
            'partsDescription'
        ]

    def create(self, validated_data):
        spare_parts_list = validated_data.pop('sparePartsList', [])

        # データベースから既存のデータを取得
        existing_parts = SpareParts.objects.filter(companyCode=validated_data['companyCode'])
        existing_parts_dict = {part.partsNo: part for part in existing_parts}

        existing_parts_nos = list(existing_parts_dict.keys())
        existing_parts_nos_int = list(map(int, existing_parts_nos))

        for part_data in spare_parts_list:
            company_code = part_data.pop('companyCode')
            parts_no = part_data.get('partsNo')

            # `orderSituation`を除くすべてのフィールドが空欄またはnullであるかをチェック
            is_row_empty = all(
                field in [None, ''] for key, field in part_data.items() if key != 'orderSituation'
            )

            if parts_no:
                if parts_no in existing_parts_dict:
                    if is_row_empty:
                        # データベースから削除
                        existing_parts_dict[parts_no].delete()
                        del existing_parts_dict[parts_no]
                    else:
                        # 更新
                        existing_part = existing_parts_dict[parts_no]
                        for key, value in part_data.items():
                            setattr(existing_part, key, value)
                        existing_part.save()
                        del existing_parts_dict[parts_no]
                elif not is_row_empty:
                    # 新規追加
                    missing_no = next((i for i in range(1, max(existing_parts_nos_int) + 2) if i not in existing_parts_nos_int), 1)
                    parts_no = str(missing_no)
                    SpareParts.objects.create(companyCode=company_code, partsNo=parts_no, **part_data)
            elif not is_row_empty:
                # 新規追加
                missing_no = next((i for i in range(1, max(existing_parts_nos_int) + 2) if i not in existing_parts_nos_int), 1)
                parts_no = str(missing_no)
                SpareParts.objects.create(companyCode=company_code, partsNo=parts_no, **part_data)

        # 残っているものは削除
        for remaining_part in existing_parts_dict.values():
            remaining_part.delete()

        return validated_data


class CompanyCodeSPSerializer(serializers.ModelSerializer):
    sparePartsList = SparePartsSerializer(many=True, source='spareParts_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'sparePartsList']

    def create(self, validated_data):
        spare_parts_data = validated_data.pop('spareParts_companyCode')
        company_code_instance = CompanyCode.objects.create(**validated_data)
        
        for spare_part_data in spare_parts_data:
            company_code_str = spare_part_data.pop('companyCode')
            company_code_instance = CompanyCode.objects.get(companyCode=company_code_str)

            parts_no = spare_part_data.get('partsNo')
            spare_part_instance = SpareParts.objects.filter(companyCode=company_code_instance, partsNo=parts_no).first()

            if spare_part_instance:
                # 更新
                serializer = SparePartsSerializer(spare_part_instance, data=spare_part_data)
                if serializer.is_valid():
                    serializer.save()
            else:
                # partsNoを自動生成
                existing_parts_nos = SpareParts.objects.values_list('partsNo', flat=True).order_by('partsNo')
                existing_parts_nos_int = [int(partsNo) for partsNo in existing_parts_nos if partsNo.isdigit()]
                if existing_parts_nos_int:
                    missing_no = next((i for i in range(1, max(existing_parts_nos_int) + 2) if i not in existing_parts_nos_int), None)
                    parts_no = missing_no if missing_no is not None else max(existing_parts_nos_int) + 1
                else:
                    parts_no = 1

                spare_part_data['partsNo'] = str(parts_no)  # partsNoを文字列として保存

                # すべてのフィールドが空欄またはnullでないことを確認（orderSituationを除外）
                if any(value for key, value in spare_part_data.items() if key != 'orderSituation'):
                    SpareParts.objects.create(companyCode=company_code_instance, **spare_part_data)
        
        return company_code_instance

    def update(self, instance, validated_data):
        spare_parts_data = validated_data.pop('spareParts_companyCode')
        existing_spare_parts = SpareParts.objects.filter(companyCode=instance)

        # 更新する部品リストの管理
        parts_no_list = [part['partsNo'] for part in spare_parts_data]

        # 削除する部品を特定
        for existing_part in existing_spare_parts:
            if existing_part.partsNo not in parts_no_list:
                existing_part.delete()

        for spare_part_data in spare_parts_data:
            parts_no = spare_part_data.get('partsNo')
            spare_part_instance = SpareParts.objects.filter(companyCode=instance, partsNo=parts_no).first()
            
            if spare_part_instance:
                # 更新
                serializer = SparePartsSerializer(spare_part_instance, data=spare_part_data)
                if serializer.is_valid():
                    serializer.save()
            else:
                # 新規作成
                company_code_str = spare_part_data.pop('companyCode')
                company_code_instance = CompanyCode.objects.get(companyCode=company_code_str)
                spare_part_data['companyCode'] = company_code_instance

                # partsNoを自動生成
                existing_parts_nos = SpareParts.objects.values_list('partsNo', flat=True).order_by('partsNo')
                existing_parts_nos_int = [int(partsNo) for partsNo in existing_parts_nos if partsNo.isdigit()]
                if existing_parts_nos_int:
                    missing_no = next((i for i in range(1, max(existing_parts_nos_int) + 2) if i not in existing_parts_nos_int), None)
                    parts_no = missing_no if missing_no is not None else max(existing_parts_nos_int) + 1
                else:
                    parts_no = 1

                spare_part_data['partsNo'] = str(parts_no)

                # すべてのフィールドが空欄またはnullでないことを確認（orderSituationを除外）
                if any(value for key, value in spare_part_data.items() if key != 'orderSituation'):
                    SpareParts.objects.create(**spare_part_data)
        
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





class SparePartsManagementSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )
    class Meta:
        model = SparePartsManagement #呼び出すモデル名
        fields = ['companyCode','companyName','plant', 'equipment','machineName','totalSparePartsCost','inventoryTurnover',]


class CompanySparePartsManagementSerializer(serializers.ModelSerializer):
    SparePartsManagementList = SparePartsManagementSerializer(many=True, source='sparePartsManagement_companyCode')#ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'SparePartsManagementList']