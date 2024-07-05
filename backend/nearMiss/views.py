from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import viewsets
from .models import NearMiss, CompanyCode, SafetyIndicators,TrendSafetyIndicators
from .serializers import (NearMissSerializer,CompanyNearMissSerializer,
                          SafetyIndicatorsSerializer,CompanySafetyIndicatorsSerializer,
                          TrendSafetyIndicatorsSerializer,CompanyTrendSafetyIndicatorsSerializer)




from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import NearMiss, CompanyCode
from .serializers import NearMissSerializer, CompanyNearMissSerializer

class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyNearMissSerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('nearMiss_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset

    def create(self, request, *args, **kwargs):
        company_code_value = request.data.get('companyCode')
        if not company_code_value:
            return Response({'error': 'Company code is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            company_code = CompanyCode.objects.get(companyCode=company_code_value)
        except CompanyCode.DoesNotExist:
            return Response({'error': f'Invalid company code: {company_code_value}'}, status=status.HTTP_400_BAD_REQUEST)

        near_miss_data = request.data.copy()
        near_miss_data['companyCode'] = company_code.pk  # 外部キーとして設定

        serializer = NearMissSerializer(data=near_miss_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # ここでシリアライザーのエラーを出力
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















class SafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = SafetyIndicators.objects.all()
    serializer_class = SafetyIndicatorsSerializer


class CompanySafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanySafetyIndicatorsSerializer

    #クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('safetyIndicators_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






class TrendSafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = TrendSafetyIndicators.objects.all()
    serializer_class = TrendSafetyIndicatorsSerializer

class CompanyTrendSafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyTrendSafetyIndicatorsSerializer

    def get_queryset(self):
        # Prefetch_related でソート順を指定
        prefetch = Prefetch(
            'trendSafetyIndicators_companyCode', 
            queryset=TrendSafetyIndicators.objects.order_by('lastUpdateDay')
        )
        queryset = CompanyCode.objects.prefetch_related(prefetch).all()
        
        # クエリパラメータでのフィルタリング
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
