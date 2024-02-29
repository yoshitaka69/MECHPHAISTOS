from rest_framework import serializers
from .models import NearMiss


class NearMissSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearMiss # 呼び出すモデル
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
        
        
    def create(self, validated_data):
        # まず、新しいインスタンスを作成します。
        new_near_miss = NearMiss.objects.create(**validated_data)

        # 'nearMissListNo' の値に基づいてレコードの数をカウントします。
        total_of_near_miss = NearMiss.objects.filter(nearMissListNo=validated_data['nearMissListNo']).count()

        # カウントした値を新しいインスタンスのフィールドに設定します。
        new_near_miss.totalOfNearMiss = total_of_near_miss
        new_near_miss.save()

        return new_near_miss
