from rest_framework import serializers

from django.db.models import Max
from .models import CeList,CompanyCode,Plant,Equipment,Machine,TypeOfPM

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

class TypeOfPMSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfPM 
        fields = '__all__'




class CeSerializer(serializers.ModelSerializer):
    ceList_id = serializers.SerializerMethodField()#連番ID

    class Meta:
        model = CeList
        fields = '__all__'

    def get_custom_id(self, obj):
        # companyCode を基に最大のカスタム ID を検索
        last_id = CeList.objects.filter(companyCode=obj.companyCode).aggregate(Max('ceList_id'))['ceList_id__max']

        # 新しいカスタム ID を生成（最初の場合は 1 から開始）
        new_id = 1 if last_id is None else last_id + 1

        return f"{obj.companyCode}-{new_id}"
    

    def create(self, validated_data):
        # カスタム ID を計算（例として 'companyCode' がモデル内に存在すると仮定）
        company_code = validated_data['companyCode']
        last_id = CeList.objects.filter(companyCode=company_code).aggregate(Max('ceList_id'))['ceList_id__max']
        new_id = 1 if last_id is None else last_id + 1

         # 新しいインスタンスを生成して保存
        instance = CeList(**validated_data, custom_id=new_id)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        # 既存のインスタンスを更新（カスタム ID は変更しない）
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance



class CompanyCodeCeSerializer(serializers.ModelSerializer):
    ceList = CeSerializer(many=True, read_only=True, source='ce_set')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ceList']

