from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import NearMiss, CompanyCode
from .serializers import NearMissSerializer, CompanyNearMissSerializer

class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

class NearMissByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NearMissSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return CompanyCode.objects.prefetch_related('nearMiss_companyCode').all()
