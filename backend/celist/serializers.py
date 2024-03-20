from rest_framework import serializers
from django.db.models import Max
from .models import CeList,CompanyCode




class CeListSerializer(serializers.ModelSerializer):
    ceList_id = serializers.SerializerMethodField()#連番ID

    class Meta:
        model = CeList
        fields = ["companyCode","companyName","plant","ceList_Id","equipment","machineName"]

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



class CompanyCodeCeListSerializer(serializers.ModelSerializer):
    ceList = CeListSerializer(many=True, read_only=True, source='ceList_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ceList']


