#このコードは、PM02、PM03、PM04、PM05の予定と実績のデータを取得、更新、保存するためのAPIを提供します。
# calculation appにsignal.pyを持っているので注意してください。


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





#----------------------------------------------------------------------------------------

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
class ActualPM02ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM02.objects.all()
    serializer_class = ActualPM02Serializer

class CompanyCodeAPM02ViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeAPM02Serializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plant_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    

    @action(detail=False, methods=['post'])
    def save_actual_pm02(self, request):
        try:
            company_code = request.data.get('companyCode')
            actual_pm02_list = request.data.get('actualPM02List')

            if not company_code or not actual_pm02_list:
                return Response({"error": "Invalid data"}, status=400)

            # フロントエンドから送信されたデータの組み合わせを取得
            frontend_records = set(
                (company_code, plant_data['plant'], year_data['year'])
                for plant_data in actual_pm02_list
                for year_data in plant_data['actualPM02']
            )

            # バックエンドの既存データを取得
            existing_records = set(
                (record.companyCode.companyCode, record.plant.plant, record.year)
                for record in ActualPM02.objects.filter(companyCode__companyCode=company_code)
            )

            # フロントエンドに存在しないバックエンドのデータを削除
            records_to_delete = existing_records - frontend_records
            for company_code, plant, year in records_to_delete:
                ActualPM02.objects.filter(
                    companyCode__companyCode=company_code,
                    plant__plant=plant,
                    year=year
                ).delete()

            # フロントエンドのデータを保存または更新
            for plant_data in actual_pm02_list:
                plant_name = plant_data.get('plant')
                for year_data in plant_data.get('actualPM02'):
                    year_data['companyCode'] = company_code
                    year_data['plant'] = plant_name
                    # 既存のレコードをチェック
                    existing_record = ActualPM02.objects.filter(
                        companyCode__companyCode=company_code,
                        plant__plant=plant_name,
                        year=year_data['year']
                    ).first()
                    if existing_record:
                        # 既存のレコードが存在する場合は更新
                        serializer = ActualPM02Serializer(existing_record, data=year_data)
                    else:
                        # 存在しない場合は新規作成
                        serializer = ActualPM02Serializer(data=year_data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=400)

            return Response({"status": "success"}, status=200)
        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=500)





#----------------------------------------------------------------------------------------






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
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeAPM03Serializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plant_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset

    @action(detail=False, methods=['post'])
    def save_actual_pm03(self, request):
        try:
            company_code = request.data.get('companyCode')
            actual_pm03_list = request.data.get('actualPM03List')

            if not company_code or not actual_pm03_list:
                return Response({"error": "Invalid data"}, status=400)

            # フロントエンドから送信されたデータの組み合わせを取得
            frontend_records = set(
                (company_code, plant_data['plant'], year_data['year'])
                for plant_data in actual_pm03_list
                for year_data in plant_data['actualPM03']
            )

            # バックエンドの既存データを取得
            existing_records = set(
                (record.companyCode.companyCode, record.plant.plant, record.year)
                for record in ActualPM03.objects.filter(companyCode__companyCode=company_code)
            )

            # フロントエンドに存在しないバックエンドのデータを削除
            records_to_delete = existing_records - frontend_records
            for company_code, plant, year in records_to_delete:
                ActualPM03.objects.filter(
                    companyCode__companyCode=company_code,
                    plant__plant=plant,
                    year=year
                ).delete()

            # フロントエンドのデータを保存または更新
            for plant_data in actual_pm03_list:
                plant_name = plant_data.get('plant')
                for year_data in plant_data.get('actualPM03'):
                    year_data['companyCode'] = company_code
                    year_data['plant'] = plant_name
                    # 既存のレコードをチェック
                    existing_record = ActualPM03.objects.filter(
                        companyCode__companyCode=company_code,
                        plant__plant=plant_name,
                        year=year_data['year']
                    ).first()
                    if existing_record:
                        # 既存のレコードが存在する場合は更新
                        serializer = ActualPM03Serializer(existing_record, data=year_data)
                    else:
                        # 存在しない場合は新規作成
                        serializer = ActualPM03Serializer(data=year_data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=400)

            return Response({"status": "success"}, status=200)
        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=500)





#----------------------------------------------------------------------------------------






#PM04-Actual
class ActualPM04ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM04.objects.all()
    serializer_class = ActualPM04Serializer

class CompanyCodeAPM04ViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeAPM04Serializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plant_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    

    @action(detail=False, methods=['post'])
    def save_actual_pm04(self, request):
        try:
            company_code = request.data.get('companyCode')
            actual_pm04_list = request.data.get('actualPM04List')

            if not company_code or not actual_pm04_list:
                return Response({"error": "Invalid data"}, status=400)

            # フロントエンドから送信されたデータの組み合わせを取得
            frontend_records = set(
                (company_code, plant_data['plant'], year_data['year'])
                for plant_data in actual_pm04_list
                for year_data in plant_data['actualPM04']
            )

            # バックエンドの既存データを取得
            existing_records = set(
                (record.companyCode.companyCode, record.plant.plant, record.year)
                for record in ActualPM04.objects.filter(companyCode__companyCode=company_code)
            )

            # フロントエンドに存在しないバックエンドのデータを削除
            records_to_delete = existing_records - frontend_records
            for company_code, plant, year in records_to_delete:
                ActualPM04.objects.filter(
                    companyCode__companyCode=company_code,
                    plant__plant=plant,
                    year=year
                ).delete()

            # フロントエンドのデータを保存または更新
            for plant_data in actual_pm04_list:
                plant_name = plant_data.get('plant')
                for year_data in plant_data.get('actualPM04'):
                    year_data['companyCode'] = company_code
                    year_data['plant'] = plant_name
                    # 既存のレコードをチェック
                    existing_record = ActualPM04.objects.filter(
                        companyCode__companyCode=company_code,
                        plant__plant=plant_name,
                        year=year_data['year']
                    ).first()
                    if existing_record:
                        # 既存のレコードが存在する場合は更新
                        serializer = ActualPM04Serializer(existing_record, data=year_data)
                    else:
                        # 存在しない場合は新規作成
                        serializer = ActualPM04Serializer(data=year_data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=400)

            return Response({"status": "success"}, status=200)
        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=500)

#----------------------------------------------------------------------------------------



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



#PM05-Actual
class ActualPM05ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM05.objects.all()
    serializer_class = ActualPM05Serializer

class CompanyCodeAPM05ViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeAPM05Serializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('plant_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    
    @action(detail=False, methods=['post'])
    def save_actual_pm05(self, request):
        try:
            company_code = request.data.get('companyCode')
            actual_pm05_list = request.data.get('actualPM05List')

            if not company_code or not actual_pm05_list:
                return Response({"error": "Invalid data"}, status=400)

            # フロントエンドから送信されたデータの組み合わせを取得
            frontend_records = set(
                (company_code, plant_data['plant'], year_data['year'])
                for plant_data in actual_pm05_list
                for year_data in plant_data['actualPM05']
            )

            # バックエンドの既存データを取得
            existing_records = set(
                (record.companyCode.companyCode, record.plant.plant, record.year)
                for record in ActualPM05.objects.filter(companyCode__companyCode=company_code)
            )

            # フロントエンドに存在しないバックエンドのデータを削除
            records_to_delete = existing_records - frontend_records
            for company_code, plant, year in records_to_delete:
                ActualPM05.objects.filter(
                    companyCode__companyCode=company_code,
                    plant__plant=plant,
                    year=year
                ).delete()

            # フロントエンドのデータを保存または更新
            for plant_data in actual_pm05_list:
                plant_name = plant_data.get('plant')
                for year_data in plant_data.get('actualPM05'):
                    year_data['companyCode'] = company_code
                    year_data['plant'] = plant_name
                    # 既存のレコードをチェック
                    existing_record = ActualPM05.objects.filter(
                        companyCode__companyCode=company_code,
                        plant__plant=plant_name,
                        year=year_data['year']
                    ).first()
                    if existing_record:
                        # 既存のレコードが存在する場合は更新
                        serializer = ActualPM05Serializer(existing_record, data=year_data)
                    else:
                        # 存在しない場合は新規作成
                        serializer = ActualPM05Serializer(data=year_data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=400)

            return Response({"status": "success"}, status=200)
        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=500)




