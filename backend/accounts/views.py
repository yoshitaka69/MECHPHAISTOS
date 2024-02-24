from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CompanyList,UserList,PaymentsList
from .serializers import CompanyListSerializer,UserListSerializer,PaymentsListSerializer


class CompanyListView(APIView):
    def get(self, request, format=None):
        companyList = CompanyList.objects.all()[0:4] 
        serializer = CompanyListSerializer(companyList, many=True)
        return Response(serializer.data)
    

class UserListView(APIView):
    def get(self, request, format=None):
        userList = UserList.objects.all()[0:4] 
        serializer = UserListSerializer(userList, many=True)
        return Response(serializer.data)
    

class PaymentsListView(APIView):
    def get(self, request, format=None):
        paymentsList = PaymentsList.objects.all()[0:4] 
        serializer = PaymentsListSerializer(paymentsList, many=True)
        return Response(serializer.data)
