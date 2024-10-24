from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import CustomUser, Company, Payment,CompanyCode,CompanyName,AreaCode,CommunityGroup,Plant
from .serializers import CustomUserSerializer, CompanySerializer, PaymentSerializer,CompanyCodeSerializer,CompanyNameSerializer,AreaCodeSerializer,CommunityGroupSerializer,CompanyCodeUserSerializer,PlantSerializer,CompanyPlantSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        customUser = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(customUser)
        return Response(serializer.data)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        company = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(company)
        return Response(serializer.data)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        payment = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(payment)
        return Response(serializer.data)

class CompanyCodeViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyCodeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        payment = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(payment)
        return Response(serializer.data)

class CompanyNameViewSet(viewsets.ModelViewSet):
    queryset = CompanyName.objects.all()
    serializer_class = CompanyNameSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        payment = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(payment)
        return Response(serializer.data)


class AreaCodeViewSet(viewsets.ModelViewSet):
    queryset = AreaCode.objects.all()
    serializer_class = AreaCodeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        payment = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(payment)
        return Response(serializer.data)
    
class CommunityGroupViewSet(viewsets.ModelViewSet):
    queryset = CommunityGroup.objects.all()
    serializer_class = CommunityGroupSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        payment = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(payment)
        return Response(serializer.data)
    


class CompanyCodeUserViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeUserSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('customUser_companyCode').all()





class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class CompanyPlantViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyPlantSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('plant_companyCode').all()




