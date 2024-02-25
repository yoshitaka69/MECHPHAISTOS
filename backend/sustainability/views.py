from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas
from .serializers import Co2Serializer,StmSerializer,ElectricityUsageSerializer,CompressedAirSerializer,WellWaterSerializer,PureWaterSerializer,WwtSerializer,ExhaustGasSerializer

    
class Co2ViewSet(viewsets.ModelViewSet):
    queryset = Co2.objects.all()
    serializer_class = Co2Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        co2 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(co2)
        return Response(serializer.data)
    
class StmViewSet(viewsets.ModelViewSet):
    queryset = Stm.objects.all()
    serializer_class = StmSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        stm = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(stm)
        return Response(serializer.data)

class ElectricityUsageViewSet(viewsets.ModelViewSet):
    queryset = ElectricityUsage.objects.all()
    serializer_class = ElectricityUsageSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        electricityUsage = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(electricityUsage)
        return Response(serializer.data)

class CompressedAirViewSet(viewsets.ModelViewSet):
    queryset = CompressedAir.objects.all()
    serializer_class = CompressedAirSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        compressedAir = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(compressedAir)
        return Response(serializer.data)
    
class WellWaterViewSet(viewsets.ModelViewSet):
    queryset = WellWater.objects.all()
    serializer_class = WellWaterSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        wellWater = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(wellWater)
        return Response(serializer.data)
    
class PureWaterViewSet(viewsets.ModelViewSet):
    queryset = PureWater.objects.all()
    serializer_class = PureWaterSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        pureWater = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(pureWater)
        return Response(serializer.data)
     
class WwtViewSet(viewsets.ModelViewSet):
    queryset = Wwt.objects.all()
    serializer_class = WwtSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        wwt = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(wwt)
        return Response(serializer.data)
    
class ExhaustGasViewSet(viewsets.ModelViewSet):
    queryset = ExhaustGas.objects.all()
    serializer_class = ExhaustGasSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        exhaustGas = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(exhaustGas)
        return Response(serializer.data)