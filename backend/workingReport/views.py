from rest_framework import viewsets
from .models import EquipmentSpecification,InspectionForm
from .serializers import EquipmentSpecificationSerializer,InspectionFormSerializer
from rest_framework.response import Response
from rest_framework import status

import pytesseract
from pdf2image import convert_from_path
import pandas as pd





class EquipmentSpecificationViewSet(viewsets.ModelViewSet):
    queryset = EquipmentSpecification.objects.all()
    serializer_class = EquipmentSpecificationSerializer





# Tesseractのインストールパスを指定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class InspectionFormViewSet(viewsets.ModelViewSet):
    queryset = InspectionForm.objects.all()
    serializer_class = InspectionFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        try:
            extracted_text = self.extract_text_from_file(instance.file.path)
            instance.extracted_text = extracted_text
            instance.save()
            headers = self.get_success_headers(serializer.data)
            return Response({**serializer.data, 'extracted_text': extracted_text}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            instance.delete()  # 保存されたファイルを削除
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def extract_text_from_file(self, file_path):
        if file_path.endswith('.pdf'):
            text = self.extract_text_from_pdf(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            text = self.extract_text_from_excel(file_path)
        elif file_path.endswith('.csv'):
            text = self.extract_text_from_csv(file_path)
        else:
            text = ""
        return text

    def extract_text_from_pdf(self, file_path):
        images = convert_from_path(file_path)
        text = ""
        for image in images:
            text += pytesseract.image_to_string(image)
        return text

    def extract_text_from_excel(self, file_path):
        df = pd.read_excel(file_path)
        text = df.to_string()
        return text

    def extract_text_from_csv(self, file_path):
        df = pd.read_csv(file_path)
        text = df.to_string()
        return text