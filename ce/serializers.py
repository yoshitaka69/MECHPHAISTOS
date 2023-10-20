#  APIの出力をJSON,XMLデータに変換
from rest_framework import serializers
from .models import CeList

class CeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CeList                     # 呼び出すモデル
        fields = ["book_name","author", "publisher","price"]  # API上に表示するモデルのデータ項目
    





