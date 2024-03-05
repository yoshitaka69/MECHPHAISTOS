from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import NearMiss, Company
from .serializers import NearMissSerializer, CompanyNearMissSerializer

class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

    # list と retrieve メソッドは ModelViewSet によって提供されるため、
    # ここではオーバーライドする必要はありません。

class NearMissByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NearMissSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return NearMiss.objects.filter(companyCode__slug=companyCode_slug)

@api_view(['GET'])
def company_near_miss_list(request):
    companies = Company.objects.all()
    serializer = CompanyNearMissSerializer(companies, many=True)
    return Response(serializer.data)
