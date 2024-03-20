from django.shortcuts import render
from rest_framework import viewsets

from .models import SpareParts
from accounts.models import CompanyCode
from .serializers import SparePartsSerializer,CompanyCodeSPSerializer


#SparePartsList
class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer

class CompanyCodeSPViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeSPSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('spareParts_companyCode').all()#ここでのrelatedNameの間違いは要注意