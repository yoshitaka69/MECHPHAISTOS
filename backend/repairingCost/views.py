from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05
from accounts.models import CompanyCode
from .serializers import PlannedPM02Serializer,CompanyCodePPM02Serializer,ActualPM02Serializer,CompanyCodeAPM02Serializer,PlannedPM03Serializer,CompanyCodePPM03Serializer,ActualPM03Serializer,CompanyCodeAPM03Serializer,ActualPM04Serializer,CompanyCodeAPM04Serializer,PlannedPM05Serializer,CompanyCodePPM05Serializer,ActualPM05Serializer,CompanyCodeAPM05Serializer


#PM02-Plan
class PlannedPM02ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM02.objects.all()
    serializer_class = PlannedPM02Serializer

class CompanyCodePPM02ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodePPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plannedPM02_companyCode').all()


#PM02-Actual
class ActualPM02ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM02.objects.all()
    serializer_class = ActualPM02Serializer

class CompanyCodeAPM02ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeAPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('actualPM02_companyCode').all()



#PM03-Planned
class PlannedPM03ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM03.objects.all()
    serializer_class = PlannedPM03Serializer

class CompanyCodePPM03ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodePPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plannedPM03_companyCode').all()



class ActualPM03ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM03.objects.all()
    serializer_class = ActualPM03Serializer

class CompanyCodeAPM03ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeAPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('actualPM03_companyCode').all()



class ActualPM04ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM04.objects.all()
    serializer_class = ActualPM04Serializer

class CompanyCodeAPM04ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeAPM04Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('actualPM04_companyCode').all()


    
class PlannedPM05ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM05.objects.all()
    serializer_class = PlannedPM05Serializer

class CompanyCodePPM05ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodePPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plannedPM05_companyCode').all()



class ActualPM05ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM05.objects.all()
    serializer_class = ActualPM05Serializer

class CompanyCodeAPM05ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeAPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('actualPM05_companyCode').all()
