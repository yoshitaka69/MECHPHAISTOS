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
    
class CompanyNearMissViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyNearMissSerializer

    def post(self, request, *args, **kwargs):
        serializer = CompanyNearMissSerializer(data=request.data)

        if serializer.is_valid():
            # NearMiss のデータを保存
            near_miss_instance = serializer.save()

            # companyCode を取得
            company_code = near_miss_instance.companyCode

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
