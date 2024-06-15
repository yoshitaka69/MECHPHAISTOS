from rest_framework import viewsets, status
from .models import ImageAnalysis
from .serializers import ImageAnalysisSerializer
from django.core.files.storage import default_storage
from tensorflow.keras.models import load_model
from rest_framework.response import Response
import numpy as np
from PIL import Image as PILImage

class ImageAnalysisViewSet(viewsets.ModelViewSet):
    queryset = ImageAnalysis.objects.all()
    serializer_class = ImageAnalysisSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            image = request.FILES['image']
            img_path = default_storage.save('tmp/' + image.name, image)

            # ここで画像を処理し、モデルで予測
            model = load_model('path_to_your_model.h5')
            img = PILImage.open(img_path)
            img = img.resize((224, 224))
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            prediction = model.predict(img_array)
            predicted_label = np.argmax(prediction, axis=1)[0]

            # 予測結果をレスポンスに含める
            return Response({
                'id': response.data['id'],
                'image': response.data['image'],
                'label': response.data['label'],
                'predicted_label': predicted_label,
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
