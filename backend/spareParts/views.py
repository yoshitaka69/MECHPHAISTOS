from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import SpareParts,Company
from .serializers import SparePartsSerializer,CompanySparePartsSerializer


#SparePartsList
class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer

class SparePartsByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SparePartsSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return SpareParts.objects.filter(companyCode__slug=companyCode_slug)

@api_view(['GET'])
def company_spareParts_list(request):
    companies = Company.objects.all()
    serializer = CompanySparePartsSerializer(companies, many=True)
    return Response(serializer.data)