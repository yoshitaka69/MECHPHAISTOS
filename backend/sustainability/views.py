from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas
from accounts.models import CompanyCode

from .serializers import Co2Serializer,CompanyCodeCo2Serializer,StmSerializer,CompanyCodeStmSerializer,ElectricityUsageSerializer,CompanyCodeElectricityUsageSerializer,CompressedAirSerializer,CompanyCodeCompressedAirSerializer,WellWaterSerializer,CompanyCodeWellWaterSerializer,PureWaterSerializer,CompanyCodePureWaterSerializer,WwtSerializer,CompanyCodeWwtSerializer,ExhaustGasSerializer,CompanyCodeExhaustGasSerializer

    
class Co2ViewSet(viewsets.ModelViewSet):
    queryset = Co2.objects.all()
    serializer_class = Co2Serializer

class CompanyCodeCo2ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeCo2Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('co2_companyCode').all()




class StmViewSet(viewsets.ModelViewSet):
    queryset = Stm.objects.all()
    serializer_class = StmSerializer

class CompanyCodeStmViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeStmSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('stm_companyCode').all()



class ElectricityUsageViewSet(viewsets.ModelViewSet):
    queryset = ElectricityUsage.objects.all()
    serializer_class = ElectricityUsageSerializer

class CompanyCodeElectricityUsageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeElectricityUsageSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('elec_companyCode').all()




class CompressedAirViewSet(viewsets.ModelViewSet):
    queryset = CompressedAir.objects.all()
    serializer_class = CompressedAirSerializer

class CompanyCodeCompressedAirViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeCompressedAirSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('compAir_companyCode').all()



class WellWaterViewSet(viewsets.ModelViewSet):
    queryset = WellWater.objects.all()
    serializer_class = WellWaterSerializer

class CompanyCodeWellWaterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeWellWaterSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('wellWater_companyCode').all()




class PureWaterViewSet(viewsets.ModelViewSet):
    queryset = PureWater.objects.all()
    serializer_class = PureWaterSerializer

class CompanyCodePureWaterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodePureWaterSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('pureWater_companyCode').all()



class WwtViewSet(viewsets.ModelViewSet):
    queryset = Wwt.objects.all()
    serializer_class = WwtSerializer

class CompanyCodeWwtViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeWwtSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('wwt_companyCode').all()




class ExhaustGasViewSet(viewsets.ModelViewSet):
    queryset = ExhaustGas.objects.all()
    serializer_class = ExhaustGasSerializer

class CompanyCodeExhaustGasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeExhaustGasSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('exhaustGas_companyCode').all()
