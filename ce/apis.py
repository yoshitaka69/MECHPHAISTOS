from .models import CeList                      # モデル呼出
from rest_framework.generics import ListCreateAPIView    # API
from .serializers import CeSerializer                # APIで渡すデータをJSON,XML変換

class api(ListCreateAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = CeList.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = CeSerializer

    # 認証
    permission_classes = []



'''認証済みの場合アクセスを許可

permission_classes = ["ここに追加したい認証機能を書き込む"]

# 読み込むメソッド
from rest_framework.permissions import IsAuthenticated

# permission_classesの書き換え
permission_classes = [IsAuthenticated]

認証済みの場合アクセスを許可'''
