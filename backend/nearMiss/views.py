from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework import status
from accounts.models import CustomUser
from .models import NearMiss, CompanyCode, ActionItemList, SafetyIndicators
from .serializers import NearMissSerializer, CompanyNearMissSerializer, ActionItemListSerializer, SafetyIndicatorsSerializer
from .service import update_safety_indicator



class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

    #nearMissインスタンスが保存されたときにsafetyIndicatorsを保存させるメソッド。
    #def perform_create(self, serializer):
        # NearMiss インスタンスを保存
        #near_miss_instance = serializer.save()
        # SafetyIndicator の更新
        #update_safety_indicator(near_miss_instance.companyCode.id)

    #def perform_update(self, serializer):
        # NearMiss インスタンスを更新
        #near_miss_instance = serializer.save()
        # SafetyIndicator の更新
        #update_safety_indicator(near_miss_instance.companyCode.id)


class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyNearMissSerializer

    
    #def create(self, request, *args, **kwargs):
        #serializer = self.get_serializer(data=request.data)
        #if serializer.is_valid():
            #company_near_miss_instance = serializer.save()
            #company_code = company_near_miss_instance.companyCode

            # サービス層の関数を呼び出して SafetyIndicator を更新⇒service層にcompanyCodeを渡す
            #update_safety_indicator(company_code)

            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class ActionItemListViewSet(viewsets.ModelViewSet):
    queryset = ActionItemList.objects.all()
    serializer_class = ActionItemListSerializer



class SafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = SafetyIndicators.objects.all()
    serializer_class = SafetyIndicatorsSerializer


