#  APIの出力をJSON,XMLデータに変換
from rest_framework import serializers
from ce.models import CeList

class CeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CeList                     # 呼び出すモデル
        fields = ["plant","equipment", "function","setting_value_impact","construction_period","parts_deliver_date","mttr","number_pm02","latest_pm02","number_pm03","latest_pm03","number_pm04","latest_pm04","impact_production","possibility_of_failure","assessment","task_pm02","cost_of_tas","period_of_task","next_event","situation_for_pm02"]  # API上に表示するモデルのデータ項目
    

