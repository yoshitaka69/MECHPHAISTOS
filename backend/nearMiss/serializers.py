from rest_framework import serializers
from .models import NearMiss
from accounts.serializers import CompanySerializer




class NearMissDetailSerializer(serializers.ModelSerializer):

    #modelとシリアライザーのデータフィールドを合わせる必要がある。
    dateOfOccurrence = serializers.DateField(format="%Y-%m-%d")
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d") 
    class Meta:
        model = NearMiss
        fields = [
            "nearMissListNo",
            "userName",
            "department",
            "dateOfOccurrence",
            "placeOfOccurrence",
            "typeOfAccident",
            "description",
            "factor",
            "injuredLv",
            "equipmentDamageLv",
            "affectOfEnviroment",
            "newsCoverage",
            "safetyIndicater",
            "measures",

            "totalOfNearMiss",

            "createdDay",
            "updateDay",
          ] # API上に表示するモデルのデータ項目

class NearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissDetailSerializer(source='*', read_only=True)
    companyCode = CompanySerializer(read_only=True)

    class Meta:
        model = NearMiss
        fields = [
            "companyCode",  # 上層に配置
            "nearMissList"#ネストされたニアミスリスト
        ]
        depth:3