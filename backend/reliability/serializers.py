from rest_framework import serializers
from .models import FailureData, WeibullData




# 故障データモデルのシリアライザー
class FailureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureData
        fields = '__all__'  # 全フィールドをシリアライズ



#ワイブルデータのシリアライザー
class WeibullDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeibullData
        fields = ['failure_time']