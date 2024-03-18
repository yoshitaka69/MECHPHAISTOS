from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import NearMiss, CompanyCode, ActionItemList, SafetyIndicators
from .serializers import NearMissSerializer, CompanyNearMissSerializer, ActionItemListSerializer, SafetyIndicatorsSerializer


class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer


# views.py
class CompanyNearMissViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyNearMissSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('nearMiss_companyCode')
        return CompanyCode.objects.all()



class ActionItemListViewSet(viewsets.ModelViewSet):
    queryset = ActionItemList.objects.all()
    serializer_class = ActionItemListSerializer


class SafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = SafetyIndicators.objects.all()
    serializer_class = SafetyIndicatorsSerializer
