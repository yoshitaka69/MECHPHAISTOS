from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from django.http import JsonResponse
from django.core.files.storage import default_storage
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image as PILImage
import io

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
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
        response.data['predicted_label'] = predicted_label
        return response
