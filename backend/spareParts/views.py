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







from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Max
from .models import SpareParts, CompanyCode
from .serializers import SparePartsSerializer


class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        sent_parts_nos = [item.get('partsNo') for item in data if item.get('partsNo') is not None]

        # 現在のデータベースに存在するpartsNoを取得
        existing_parts_nos = list(SpareParts.objects.values_list('partsNo', flat=True))

        # 削除する必要があるpartsNoを特定
        parts_nos_to_delete = set(existing_parts_nos) - set(sent_parts_nos)

        # 削除処理
        if parts_nos_to_delete:
            SpareParts.objects.filter(partsNo__in=parts_nos_to_delete).delete()

        # 新規作成または更新の処理
        created_items = []
        for item in data:
            company_code_str = item.get('companyCode')

            # companyCodeが文字列として渡された場合、それに対応するオブジェクトを取得
            try:
                company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
                item['companyCode'] = company_code_obj.id  # IDに変換
            except CompanyCode.DoesNotExist:
                return Response(
                    {"error": f"CompanyCode '{company_code_str}' does not exist."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            parts_no = item.get('partsNo')

            if parts_no is not None:
                # partsNoが存在する場合、既存のレコードを更新する
                existing_item = SpareParts.objects.filter(partsNo=parts_no).first()
                if existing_item:
                    serializer = self.get_serializer(existing_item, data=item, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    created_items.append(serializer.data)
                    continue  # 更新処理をした場合は次のアイテムに進む

            # partsNoがnullまたは新規作成の場合
            if parts_no is None:
                # 最大のpartsNoを取得し、そこから次の番号を割り当てる
                max_parts_no = SpareParts.objects.aggregate(Max('partsNo'))['partsNo__max'] or "00000"
                max_parts_no = int(max_parts_no)  # 整数に変換
                item['partsNo'] = str(max_parts_no + 1).zfill(5)  # 整数を文字列に変換してゼロ埋め

            serializer = self.get_serializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            created_items.append(serializer.data)

        return Response(created_items, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        parts_no = request.data.get('partsNo')
        if parts_no:
            try:
                # partsNoに基づいて既存の部品を取得し、削除を試みる
                spare_part = SpareParts.objects.get(partsNo=parts_no)
                self.perform_destroy(spare_part)
                print("Delete request received with partsNo:", parts_no)
                return Response(status=status.HTTP_204_NO_CONTENT)
            except SpareParts.DoesNotExist:
                return Response({"error": "Spare Part with partsNo not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "partsNo not provided."}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()






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
