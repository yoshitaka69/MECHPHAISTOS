# views.py

from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .models import SpareParts, BomList, SparePartsManagement
from accounts.models import CompanyCode
from .serializers import (
    SparePartsSerializer, CompanyCodeSPSerializer, 
    BomListSerializer, CompanyBomListSerializer, 
    SparePartsManagementSerializer, CompanySparePartsManagementSerializer
)



# SparePartsのViewSet
#------------------------------------------------------------------------------------------------------------------
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .models import SpareParts, CompanyCode
from .serializers import SparePartsSerializer, CompanyCodeSPSerializer
from rest_framework.decorators import action

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import io



class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer

    @action(detail=False, methods=['post'], url_path='bulk-update')
    def bulk_update(self, request):
        spare_parts_list = request.data.get('sparePartsList', [])

        created_items = []
        updated_items = []

        for item_data in spare_parts_list:
            parts_no = item_data.get('partsNo')
            company_code = item_data.get('companyCode')

            spare_part = SpareParts.objects.filter(partsNo=parts_no, companyCode=company_code).first()

            if spare_part:
                serializer = SparePartsSerializer(spare_part, data=item_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_items.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = SparePartsSerializer(data=item_data)
                if serializer.is_valid():
                    serializer.save()
                    created_items.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'created': created_items,
            'updated': updated_items
        }, status=status.HTTP_200_OK)
    





class CompanyCodeSPViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeSPSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('spareParts_companyCode')
        return CompanyCode.objects.all()

@api_view(['POST'])
def upload_image(request):
    if 'image' in request.FILES:
        image = request.FILES['image']
        
        # 画像を開く
        img = Image.open(image)
        
        # 画像をリサイズ（例: 幅を150pxに）
        img.thumbnail((150, 150))
        
        # 新しい画像を保存するためのバッファ
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        
        # バッファをInMemoryUploadedFileに変換
        image = InMemoryUploadedFile(buffer, None, 'thumbnail.jpg', 'image/jpeg', buffer.tell, None)
        
        # 画像を保存
        file_path = default_storage.save(f'images/{image.name}', image)
        image_url = default_storage.url(file_path)
        return Response({'imageUrl': image_url})
    
    return Response({'error': 'Invalid request'}, status=400)

#------------------------------------------------------------------------------------------------------------------










# BomListのViewSet
class BomListViewSet(viewsets.ModelViewSet):
    queryset = BomList.objects.all()
    serializer_class = BomListSerializer

# CompanyCodeに関連するBomListのViewSet
class CompanyBomListViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyBomListSerializer

    # クエリパラメータに基づいてクエリセットをフィルタリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('bomList_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



# SparePartsManagementのViewSet
class SparePartsManagementViewSet(viewsets.ModelViewSet):
    queryset = SparePartsManagement.objects.all()
    serializer_class = SparePartsManagementSerializer

# CompanyCodeに関連するSparePartsManagementのViewSet
class CompanySparePartsManagementViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanySparePartsManagementSerializer

    # クエリパラメータに基づいてクエリセットをフィルタリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('sparePartsManagement_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
