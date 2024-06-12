from rest_framework import viewsets
from .models import FailureData, WeibullData
from .serializers import FailureDataSerializer, WeibullDataSerializer
from django.http import JsonResponse
import numpy as np

# FailureDataモデルのビューセット
class FailureDataViewSet(viewsets.ModelViewSet):
    queryset = FailureData.objects.all()  # すべてのFailureDataインスタンスをクエリ
    serializer_class = FailureDataSerializer  # 使用するシリアライザー

# 故障予測を行うビュー
def predict_failure(request):
    # 1月から12月までの月を表す配列
    months = np.arange(1, 13)
    # 各月に対応するランダムな故障発生確率の配列を生成
    probabilities = np.random.rand(12)
    # JSON形式でレスポンスを返す
    return JsonResponse({
        'months': months.tolist(),  # 月の配列をリストに変換
        'probabilities': probabilities.tolist(),  # 確率の配列をリストに変換
    })





#ワイブルデータ
class WeibullDataViewSet(viewsets.ModelViewSet):
    queryset = WeibullData.objects.all()
    serializer_class = WeibullDataSerializer