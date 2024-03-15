from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import NearMiss, CompanyCode, ActionItemList, SafetyIndicators
from .serializers import NearMissSerializer, CompanyNearMissSerializer, ActionItemListSerializer, SafetyIndicators


class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

class CompanyNearMissViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyNearMissSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('nearMiss_companyCode').all()


class ActionItemListVieset(viewsets.ModelViewSet):
    queryset = ActionItemList.objects.all()
    serializer_class = ActionItemsListSerializer

class SafetyindicatorsVieset(viewsets.ModelViewSet):
    queryset = Safetyindicators.objects.all()
    serializer_class = SafetyindicatorsSerializer
