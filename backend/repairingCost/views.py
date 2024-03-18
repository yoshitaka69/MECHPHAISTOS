from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Pm02,Pm03,Pm04,Pm05
from .serializers import Pm02Serializer,Pm03Serializer,Pm04Serializer,Pm05Serializer


class Pm02ViewSet(viewsets.ModelViewSet):
    queryset = Pm02.objects.all()
    serializer_class = Pm02Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            queryset = queryset.filter(companyCode__code=company_code)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pm02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(pm02)
        return Response(serializer.data)

    
class Pm03ViewSet(viewsets.ModelViewSet):
    queryset = Pm03.objects.all()
    serializer_class = Pm03Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            queryset = queryset.filter(companyCode__code=company_code)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pm02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(pm02)
        return Response(serializer.data)



class Pm04ViewSet(viewsets.ModelViewSet):
    queryset = Pm04.objects.all()
    serializer_class = Pm04Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            queryset = queryset.filter(companyCode__code=company_code)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pm02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(pm02)
        return Response(serializer.data)



class Pm05ViewSet(viewsets.ModelViewSet):
    queryset = Pm05.objects.all()
    serializer_class = Pm05Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            queryset = queryset.filter(companyCode__code=company_code)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pm02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(pm02)
        return Response(serializer.data)
