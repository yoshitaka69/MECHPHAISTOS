from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

import logging
from rest_framework.decorators import action
import json
from django.views.decorators.csrf import csrf_exempt



from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05
from accounts.models import CompanyCode,Plant
from .serializers import PlannedPM02Serializer,CompanyCodePPM02Serializer,ActualPM02Serializer,CompanyCodeAPM02Serializer,PlannedPM03Serializer,CompanyCodePPM03Serializer,ActualPM03Serializer,CompanyCodeAPM03Serializer,ActualPM04Serializer,CompanyCodeAPM04Serializer,PlannedPM05Serializer,CompanyCodePPM05Serializer,ActualPM05Serializer,CompanyCodeAPM05Serializer
logger = logging.getLogger(__name__)




#PM02-Plan
class PlannedPM02ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM02.objects.all()
    serializer_class = PlannedPM02Serializer

class CompanyCodePPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodePPM02Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plannedPM02_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset








#PM02-Actual
# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ActualPM02
from .serializers import ActualPM02Serializer
from rest_framework.exceptions import ValidationError

class ActualPM02ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM02.objects.all()
    serializer_class = ActualPM02Serializer

    def create(self, request, *args, **kwargs):
        data = request.data
        print("Received Data:", data)  # 受け取ったデータをログに出力

        # データがリスト形式であることを確認
        if not isinstance(data, list):
            print("Error: Data is not a list.")  # エラーログ
            return Response({"error": "Invalid data format. Expected a list of records."}, status=status.HTTP_400_BAD_REQUEST)

        # 各レコードを個別に保存・更新
        for item in data:
            print("Processing Item:", item)  # 各レコードのログ

            # plantとyearの組み合わせで既存データを検索
            plant = item.get('plant')
            year = item.get('year')

            # データベースでplantとyearが一致するデータを検索
            existing_record = ActualPM02.objects.filter(plant=plant, year=year).first()

            if existing_record:
                # 既存データがあれば、更新を行う
                print(f"Updating record for plant: {plant}, year: {year}")
                serializer = self.get_serializer(existing_record, data=item)
            else:
                # 既存データがなければ、新規追加を行う
                print(f"Creating new record for plant: {plant}, year: {year}")
                serializer = self.get_serializer(data=item)

            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
                print("Item Saved Successfully:", item)  # 保存成功時のログ
            except ValidationError as e:
                print("Validation Error:", serializer.errors)  # バリデーションエラーのログ
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        print("All Items Processed Successfully")  # 全レコードが成功した場合のログ
        return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)





class CompanyCodeAPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAPM02Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('actualPM02_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#PM03-Planned
class PlannedPM03ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM03.objects.all()
    serializer_class = PlannedPM03Serializer

class CompanyCodePPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodePPM03Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plannedPM03_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




#PM03-Actual
class ActualPM03ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM03.objects.all()
    serializer_class = ActualPM03Serializer

class CompanyCodeAPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAPM03Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('actualPM03_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



class ActualPM04ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM04.objects.all()
    serializer_class = ActualPM04Serializer

class CompanyCodeAPM04ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAPM04Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('actualPM04_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset


    

class PlannedPM05ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM05.objects.all()
    serializer_class = PlannedPM05Serializer

class CompanyCodePPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodePPM05Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plannedPM05_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset



class ActualPM05ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM05.objects.all()
    serializer_class = ActualPM05Serializer

class CompanyCodeAPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAPM05Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('actualPM05_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset