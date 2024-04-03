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
    
    def post(self, request, *args, **kwargs):
        for company_data in request.data:
            company_code = company_data.get('companyCode')
            near_misses = company_data.get('nearMissList', [])

            # 会社コードの処理
            company, created = CompanyCode.objects.get_or_create(companyCode=company_code)

            for near_miss_data in near_misses:
                user_data = near_miss_data.pop('userName', {})
                user_name = user_data.get('userName')

                # ユーザーデータの処理
                user, created = CustomUser.objects.get_or_create(userName=user_name)

                # ニアミスレポートの処理
                near_miss_data['userName'] = user
                near_miss, created = NearMiss.objects.update_or_create(
                    nearMissNo=near_miss_data['nearMissNo'],
                    defaults=near_miss_data
                )
                # 会社にニアミスレポートをリンクする
                near_miss.companyCode = company
                near_miss.save()

        return Response({"message": "データが正常に処理されました"}, status=status.HTTP_200_OK)




# views.py
class CompanyNearMissViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyNearMissSerializer

    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)
        if company_code is not None:
            return CompanyCode.objects.filter(companyCode=company_code).prefetch_related('nearMiss_companyCode')
        return CompanyCode.objects.all()






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
