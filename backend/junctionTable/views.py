from django.shortcuts import render
from rest_framework import viewsets

from .models import MasterDataTable,BomAndTask,CeListAndTask,BadActorManagement,EventYearPPM,GapOfRepairingCost
from accounts.models import CompanyCode
from .serializers import  (MasterDataTableSerializer, CompanyCodeMDTSerializer,
                           BomAndTaskSerializer,CompanyCodeBomAndTaskSerializer,
                           CeListAndTaskSerializer,CompanyCodeCeListAndTaskSerializer,
                           BadActorManagementSerializer,CompanyCodeBadActorSerializer,
                           EventYearPPMSerializer,CompanyCodeEventYearPPMSerializer,
                           GapOfRepairingCostSerializer,CompanyCodeGapOfRepairingCostSerializer,)


#MasterDataTable
class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer


class CompanyCodeMDTViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeMDTSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('masterDataTable_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#BomAndTask
class BomAndTaskViewSet(viewsets.ModelViewSet):
    queryset = BomAndTask.objects.all()
    serializer_class = BomAndTaskSerializer


class CompanyCodeBomAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeBomAndTaskSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('bomAndTask_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#CeListAndTask
class CeListAndTaskViewSet(viewsets.ModelViewSet):
    queryset = CeListAndTask.objects.all()
    serializer_class = CeListAndTaskSerializer


class CompanyCodeCeListAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCeListAndTaskSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('ceListAndTask_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




#BadActorManagement
class BadActorManagementViewSet(viewsets.ModelViewSet):
    queryset = BadActorManagement.objects.all()
    serializer_class = BadActorManagementSerializer

class CompanyCodeBadActorViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeBadActorSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('badActorManagement_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




class EventYearPPMViewSet(viewsets.ModelViewSet):
    queryset = EventYearPPM.objects.all()
    serializer_class = EventYearPPMSerializer

class CompanyCodeEventYearPPMViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeEventYearPPMSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('eventYearPPM_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    




class GapOfRepairingCostViewSet(viewsets.ModelViewSet):
    queryset = GapOfRepairingCost.objects.all()
    serializer_class = GapOfRepairingCostSerializer

class CompanyCodeGapOfRepairingCostViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeGapOfRepairingCostSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('gapOfRepairingCost_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset