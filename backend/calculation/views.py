from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import CompanyCode

from .models import (CalTablePlannedPM02,CalTableActualPM02,
                     CalTablePlannedPM03,CalTableActualPM03,
                     CalTableActualPM04,
                     CalTablePlannedPM05,CalTableActualPM05,
                     SummedPlannedCost,
                     SummedActualCost)

from .serializers import (CalTablePPM02Serializer,CalTableAPM02Serializer,
                          CompanyCodeCalPPM02Serializer,CompanyCodeCalAPM02Serializer,

                          CalTablePPM03Serializer,CalTableAPM03Serializer,
                          CompanyCodeCalPPM03Serializer,CompanyCodeCalAPM03Serializer,

                          CalTableAPM04Serializer,
                          CompanyCodeCalAPM04Serializer,

                          CalTablePPM05Serializer,CalTableAPM05Serializer,
                          CompanyCodeCalPPM05Serializer,CompanyCodeCalAPM05Serializer,

                          SummedPlannedCostSerializer,CompanyCodeSummedPlannedCostSerializer,
                          SummedActualCostSerializer,CompanyCodeSummedActualCostSerializer)


#PlannedPM02
class CalTablePPM02ViewSet(viewsets.ModelViewSet):
    queryset = CalTablePlannedPM02.objects.all()
    serializer_class = CalTablePPM02Serializer

class CompanyCodeCalTablePPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalPPM02Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTablePlannedPM02_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#ActualPM02
class CalTableAPM02ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM02.objects.all()
    serializer_class = CalTableAPM02Serializer

class CompanyCodeCalTableAPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM02Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM02_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#plannedPM03
class CalTablePPM03ViewSet(viewsets.ModelViewSet):
    queryset = CalTablePlannedPM03.objects.all()
    serializer_class = CalTablePPM03Serializer

class CompanyCodeCalTablePPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalPPM03Serializer

  
#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTablePlannedPM03_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#actualPM03
class CalTableAPM03ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM03.objects.all()
    serializer_class = CalTableAPM03Serializer

class CompanyCodeCalTableAPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM03Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM03_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#actualPM04
class CalTableAPM04ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM04.objects.all()
    serializer_class = CalTableAPM04Serializer

class CompanyCodeCalTableAPM04ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM04Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM04_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#plannedPM05
class CalTablePPM05ViewSet(viewsets.ModelViewSet):
    queryset = CalTablePlannedPM05.objects.all()
    serializer_class = CalTablePPM05Serializer

class CompanyCodeCalTablePPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalPPM05Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTablePlannedPM05_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#actualPM05
class CalTableAPM05ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM05.objects.all()
    serializer_class = CalTableAPM05Serializer

class CompanyCodeCalTableAPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM05Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM05_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    
    



#SummedPlannedCost
class SummedPlannedCostViewSet(viewsets.ModelViewSet):
    queryset = SummedPlannedCost.objects.all()
    serializer_class = SummedPlannedCostSerializer


class CompanyCodeSummedPlannedCostViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeSummedPlannedCostSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('summedPlannedCost_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#SummedActualCost
class SummedActualCostViewSet(viewsets.ModelViewSet):
    queryset = SummedActualCost.objects.all()
    serializer_class = SummedActualCostSerializer


class CompanyCodeSummedActualCostViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeSummedActualCostSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('summedActualCost_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
