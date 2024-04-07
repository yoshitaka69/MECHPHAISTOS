
from rest_framework import viewsets
from .models import NearMiss, CompanyCode, SafetyIndicators
from .serializers import NearMissSerializer, CompanyNearMissSerializer, SafetyIndicatorsSerializer




class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer


class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyNearMissSerializer


class SafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = SafetyIndicators.objects.all()
    serializer_class = SafetyIndicatorsSerializer


