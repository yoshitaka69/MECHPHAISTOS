# 必要なモジュールとクラスをインポート
from django.urls import path, include  # URLパターンを定義するために使用
from rest_framework.routers import DefaultRouter  # ビューセットをルーターに登録するために使用
from .views import FailureDataViewSet, predict_failure, WeibullDataViewSet  # アプリ内のビューをインポート

# ルーターのインスタンスを作成
router = DefaultRouter()

# 'failuredata'エンドポイントをFailureDataViewSetビューセットに登録
# basename='reliability'はURL逆引きの際に使用される名前
router.register(r'failuredata', FailureDataViewSet, basename='reliability')

# 'weibull-data'エンドポイントをWeibullDataViewSetビューセットに登録
router.register(r'weibull-data', WeibullDataViewSet)

# URLパターンを定義
urlpatterns = [
    # ルーターで定義された全てのURLを含める
    path('', include(router.urls)),
    
    # 'reliability/predict/'エンドポイントをpredict_failureビュー関数にマッピング
    # name='predict_failure'はこのURLパターンの名前
    path('reliability/predict/', predict_failure, name='predict_failure'),
]
