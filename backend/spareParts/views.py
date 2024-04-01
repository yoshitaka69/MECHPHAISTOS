from django.shortcuts import render
from rest_framework import viewsets

from .models import SpareParts
from accounts.models import CompanyCode
from .serializers import SparePartsSerializer,CompanyCodeSPSerializer




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
class BomCodeViewSet(viewsets.ModelViewSet):
    queryset = BomCode.objects.all()
    serializer_class = BomCodeSerializer

class CompanyBomCodeViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyBomCodeSerializer

    #これで無駄なデータのやり取りをなくす。
    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('bomCode_companyCode').all()

