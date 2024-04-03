from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import status
from accounts.models import CustomUser
from .models import NearMiss, CompanyCode, ActionItemList, SafetyIndicators
from .serializers import NearMissSerializer, CompanyNearMissSerializer, ActionItemListSerializer, SafetyIndicatorsSerializer




class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer
    
class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyNearMissSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            company_near_miss_instance = serializer.save()
            company_code = company_near_miss_instance.companyCode

            # サービス層の関数を呼び出して SafetyIndicator を更新
            safety_indicator_service.update_safety_indicator(company_code)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class ActionItemListViewSet(viewsets.ModelViewSet):
    queryset = ActionItemList.objects.all()
    serializer_class = ActionItemListSerializer



class SafetyIndicatorView(views.APIView):
    def post(self, request, *args, **kwargs):
        print("リクエストデータ:", request.data)  # デバッグ情報

        company_code = request.data.get('companyCode')

        serializer = SafetyIndicatorsSerializer(data=request.data)
        if serializer.is_valid():
            SafetyIndicators.update_total_of_near_miss(company_code)
            print("更新された companyCode:", company_code)  # デバッグ情報
            return Response(serializer.data, status=201)
        else:
            print("エラー:", serializer.errors)  # デバッグ情報
            return Response(serializer.errors, status=400)
