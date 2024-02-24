from rest_framework import serializers
from .models import RepairingCostPM02


class RepairingCostPM02Serializer(serializers.ModelSerializer):
    class Meta:
        model = RepairingCostPM02 # 呼び出すモデル
        fields = [
            "plant",
            "plannedPM02",
        ] # API上に表示するモデルのデータ項目
