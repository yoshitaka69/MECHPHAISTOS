from django.shortcuts import render
from rest_framework import viewsets

from .models import SpareParts,BomList,SparePartsManagement
from accounts.models import CompanyCode
from .serializers import SparePartsSerializer,CompanyCodeSPSerializer,BomListSerializer,CompanyBomListSerializer,SparePartsManagementSerializer,CompanySparePartsManagementSerializer




#SparePartsList
class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer


class CompanyCodeSPViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeSPSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('spareParts_companyCode')
        return CompanyCode.objects.all()


#BomCode
class BomListViewSet(viewsets.ModelViewSet):
    queryset = BomList.objects.all()
    serializer_class = BomListSerializer

class CompanyBomListViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyBomListSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('bomList_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset




#SparePartsManagement
class SparePartsManagementViewSet(viewsets.ModelViewSet):
    queryset = SparePartsManagement.objects.all()
    serializer_class = SparePartsManagementSerializer

class CompanySparePartsManagementViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanySparePartsManagementSerializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('sparePartsManagement_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset