from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas
from accounts.models import CompanyCode,Plant

from .serializers import (Co2Serializer,PlantCo2Serializer,CompanyCodeCo2Serializer,
                          StmSerializer,CompanyCodeStmSerializer,PlantStmSerializer,
                          ElecSerializer,CompanyCodeElecSerializer,PlantElecSerializer,
                          CompAirSerializer,CompanyCodeCompAirSerializer,PlantCompAirSerializer,
                          WellWaterSerializer,CompanyCodeWellWaterSerializer,PlantWellWaterSerializer,
                          PureWaterSerializer,CompanyCodePureWaterSerializer,PlantPureWaterSerializer,
                          WwtSerializer,CompanyCodeWwtSerializer,PlantWwtSerializer,
                          ExhaustGasSerializer,CompanyCodeExhaustGasSerializer,PlantExhaustGasSerializer)

    
class Co2ViewSet(viewsets.ModelViewSet):
    queryset = Co2.objects.all()
    serializer_class = Co2Serializer

    def get_queryset(self):
        queryset = Co2.objects.all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            queryset = queryset.filter(companyCode__code=company_code)
        return queryset


class PlantCo2ViewSet(viewsets.ModelViewSet):
    serializer_class = PlantCo2Serializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeCo2ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeCo2Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('co2_companyCode').all()






#STM
class StmViewSet(viewsets.ModelViewSet):
    queryset = Stm.objects.all()
    serializer_class = StmSerializer
  
    def get_queryset(self):
      queryset = Stm.objects.all()
      company_code = self.request.query_params.get('companyCode', None)
      if company_code is not None:
          queryset = queryset.filter(companyCode__code=company_code)
      return queryset


class PlantStmViewSet(viewsets.ModelViewSet):
    serializer_class = PlantStmSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeStmViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeStmSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('stm_companyCode').all()








#elec
class ElecViewSet(viewsets.ModelViewSet):
    queryset = ElectricityUsage.objects.all()
    serializer_class = ElecSerializer

    def get_queryset(self):
        queryset = ElectricityUsage.objects.all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            queryset = queryset.filter(companyCode__code=company_code)
        return queryset
  

class PlantElecViewSet(viewsets.ModelViewSet):
    serializer_class = PlantElecSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeElecViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeElecSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('elec_companyCode').all()






#compAir
class CompAirViewSet(viewsets.ModelViewSet):
    queryset = CompressedAir.objects.all()
    serializer_class = CompAirSerializer

    def get_queryset(self):
      queryset = CompressedAir.objects.all()
      company_code = self.request.query_params.get('companyCode', None)
      if company_code is not None:
          queryset = queryset.filter(companyCode__code=company_code)
      return queryset

class PlantCompAirViewSet(viewsets.ModelViewSet):
    serializer_class = PlantCompAirSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeCompAirViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeCompAirSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plant_companyCode').all()




#WellWater
class WellWaterViewSet(viewsets.ModelViewSet):
    queryset = WellWater.objects.all()
    serializer_class = WellWaterSerializer

    def get_queryset(self):
      queryset = WellWater.objects.all()
      company_code = self.request.query_params.get('companyCode', None)
      if company_code is not None:
          queryset = queryset.filter(companyCode__code=company_code)
      return queryset

class PlantWellWaterViewSet(viewsets.ModelViewSet):
    serializer_class = PlantWellWaterSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeWellWaterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeWellWaterSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plant_companyCode').all()




#PureWater
class PureWaterViewSet(viewsets.ModelViewSet):
    queryset = PureWater.objects.all()
    serializer_class = PureWaterSerializer

    def get_queryset(self):
      queryset = PureWater.objects.all()
      company_code = self.request.query_params.get('companyCode', None)
      if company_code is not None:
          queryset = queryset.filter(companyCode__code=company_code)
      return queryset

class PlantPureWaterViewSet(viewsets.ModelViewSet):
    serializer_class = PlantPureWaterSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodePureWaterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodePureWaterSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plant_companyCode').all()






#Wwt
class WwtViewSet(viewsets.ModelViewSet):
    queryset = Wwt.objects.all()
    serializer_class = WwtSerializer

    def get_queryset(self):
      queryset = Wwt.objects.all()
      company_code = self.request.query_params.get('companyCode', None)
      if company_code is not None:
          queryset = queryset.filter(companyCode__code=company_code)
      return queryset


class PlantWwtViewSet(viewsets.ModelViewSet):
    serializer_class = PlantWwtSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeWwtViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeWwtSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plant_companyCode').all()




#ExhaustGas
class ExhaustGasViewSet(viewsets.ModelViewSet):
    queryset = ExhaustGas.objects.all()
    serializer_class = ExhaustGasSerializer

    def get_queryset(self):
      queryset = ExhaustGas.objects.all()
      company_code = self.request.query_params.get('companyCode', None)
      if company_code is not None:
          queryset = queryset.filter(companyCode__code=company_code)
      return queryset

class PlantExhaustGasViewSet(viewsets.ModelViewSet):
    serializer_class = PlantExhaustGasSerializer

    def get_queryset(self):
        # 'plant' フィールドに基づいて昇順に並べ替え
        return Plant.objects.order_by('plant')

class CompanyCodeExhaustGasViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeExhaustGasSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plant_companyCode').all()
