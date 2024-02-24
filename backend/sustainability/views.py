from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Co2List,StmList,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas
from .serializers import Co2ListSerializer,StmListSerializer,ElectricityUsageSerializer,CompressedAirSerializer,WellWaterSerializer,PureWaterSerializer,WwtSerializer,ExhaustGasSerializer

class Co2ListView(APIView):
    def get(self, request, format=None):
        co2List = Co2List.objects.all()[0:4] 
        serializer = Co2ListSerializer(co2List, many=True)
        return Response(serializer.data)


class StmListView(APIView):
    def get(self, request, format=None):
        stmList = StmList.objects.all()[0:4] 
        serializer = StmListSerializer(stmList, many=True)
        return Response(serializer.data)


class ElectricityUsageView(APIView):
    def get(self, request, format=None):
        electricityUsage = ElectricityUsage.objects.all()[0:4] 
        serializer = ElectricityUsageSerializer(electricityUsage, many=True)
        return Response(serializer.data)
    
    
class CompressedAirView(APIView):
    def get(self, request, format=None):
        compressedAir = CompressedAir.objects.all()[0:4] 
        serializer = CompressedAirSerializer(compressedAir, many=True)
        return Response(serializer.data)


class WellWaterView(APIView):
    def get(self, request, format=None):
        wellWater = WellWater.objects.all()[0:4] 
        serializer = WellWaterSerializer(wellWater, many=True)
        return Response(serializer.data)
    

class PureWaterView(APIView):
    def get(self, request, format=None):
        pureWater = PureWater.objects.all()[0:4] 
        serializer = PureWaterSerializer(pureWater, many=True)
        return Response(serializer.data)
    

class WwtView(APIView):
    def get(self, request, format=None):
        wwt = Wwt.objects.all()[0:4] 
        serializer = WwtSerializer(wwt, many=True)
        return Response(serializer.data)
        

class ExhaustGasView(APIView):
    def get(self, request, format=None):
        exhaustGas = ExhaustGas.objects.all()[0:4] 
        serializer = ExhaustGasSerializer(exhaustGas, many=True)
        return Response(serializer.data)