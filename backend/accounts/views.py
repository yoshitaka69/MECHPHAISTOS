from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import CustomUser, Company, UserInfo, Payment
from .serializers import CustomUserSerializer, CompanySerializer, UserInfoSerializer, PaymentSerializer

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

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        userInfo = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(userInfo)
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