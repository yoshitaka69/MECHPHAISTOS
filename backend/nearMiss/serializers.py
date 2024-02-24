from rest_framework import serializers
from .models import NearMissList


class NearMissListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearMissList # 呼び出すモデル
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
            "createdDay",
            "updateDay",
          ] # API上に表示するモデルのデータ項目