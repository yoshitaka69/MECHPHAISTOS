from rest_framework import viewsets, status
from .models import ImageAnalysis
from .serializers import ImageAnalysisSerializer
from django.core.files.storage import default_storage
from tensorflow.keras.models import load_model
from rest_framework.response import Response
import numpy as np
from PIL import Image as PILImage
import os

# 絶対パスを使用してモデルファイルのパスを設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models/model.h5')

class ImageAnalysisViewSet(viewsets.ModelViewSet):
    queryset = ImageAnalysis.objects.all()
    serializer_class = ImageAnalysisSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            image = request.FILES['image']
            tmp_dir = os.path.join(BASE_DIR, 'media/tmp')
            
            # tmpディレクトリが存在しない場合は作成
            if not os.path.exists(tmp_dir):
                os.makedirs(tmp_dir)
            
            img_path = default_storage.save(os.path.join('tmp', image.name), image)

            # 実際のファイルパスを取得
            img_full_path = default_storage.path(img_path)

            # ここで画像を処理し、モデルで予測
            model = load_model(MODEL_PATH)
            img = PILImage.open(img_full_path).convert('RGB')  # カラー画像として開く
            img = img.resize((224, 224))  # モデルが期待する入力サイズにリサイズ
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_array)
            predicted_label = np.argmax(prediction, axis=1)[0]

            # 予測結果をレスポンスに含める
            return Response({
                'id': response.data['id'],
                'image': f'/media/{img_path}',
                'label': response.data['label'],
                'predicted_label': predicted_label,
                'predicted_class': train_generator.class_indices[predicted_label]  # クラス名を追加
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
