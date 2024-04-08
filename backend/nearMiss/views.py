
from rest_framework import viewsets
from .models import NearMiss, CompanyCode, SafetyIndicators,TrendSafetyIndicators
from .serializers import (NearMissSerializer,CompanyNearMissSerializer,
                          SafetyIndicatorsSerializer,CompanySafetyIndicatorsSerializer,
                          TrendSafetyIndicatorsSerializer,CompanyTrendSafetyIndicatorsSerializer)




class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer


class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyNearMissSerializer






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

    #クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('trendSafetyIndicators_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
