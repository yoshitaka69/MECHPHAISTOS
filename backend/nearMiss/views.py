from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import NearMiss
from .serializers import NearMissSerializer


class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        nearMiss = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(nearMiss)
        return Response(serializer.data)
    
    
class NearMissByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NearMissSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return NearMiss.objects.filter(companyCode__slug=companyCode_slug)