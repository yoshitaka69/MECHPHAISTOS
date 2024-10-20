from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

# 使用するモデル
from .models import (
    NearMiss, 
    CompanyCode, 
    SafetyIndicators, 
    TrendSafetyIndicators, 
    CustomUser
)

# 使用するシリアライザ
from .serializers import (
    NearMissSerializer, 
    CompanyNearMissSerializer,
    SafetyIndicatorsSerializer, 
    CompanySafetyIndicatorsSerializer,
    TrendSafetyIndicatorsSerializer, 
    CompanyTrendSafetyIndicatorsSerializer
)

from django.http import Http404

#----------------------------------------------------------------------------------------------------------------------------------------------

class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

    def get_object(self):
        near_miss_no = self.kwargs.get('pk')  # URLのパスから<id>を取得する
        company_code_str = self.request.data.get('companyCode')

        if not near_miss_no or not company_code_str:
            raise Http404("NearMissNo or CompanyCode missing")

        try:
            return NearMiss.objects.get(companyCode__companyCode=company_code_str, nearMissNo=near_miss_no)
        except NearMiss.DoesNotExist:
            raise Http404("NearMiss not found with given NearMissNo and CompanyCode")


    def create(self, request, *args, **kwargs):
        data = request.data
        print(f"Received data: {data}")

        # companyCode を取得
        company_code_str = data.get('companyCode')

        # companyCode が存在しない場合はエラーレスポンスを返す
        if not company_code_str:
            return Response(
                {"error": "companyCode is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        print(f"Received companyCode: {company_code_str}")

        # companyCode を CompanyCode オブジェクトとして取得する
        try:
            company_code_obj = CompanyCode.objects.get(companyCode=company_code_str)
        except CompanyCode.DoesNotExist:
            return Response(
                {"error": f"CompanyCode '{company_code_str}' does not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 新規NearMissの作成処理
        print("Creating a new NearMiss.")

        # `nearMissNo`はPOSTデータから受け取らず、モデルで自動生成
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        created_near_miss = self.perform_create(serializer)

        # 作成されたNearMissオブジェクトから`nearMissNo`を取得して返す
        return Response({
            "nearMissNo": created_near_miss.nearMissNo,
            "message": "NearMiss created successfully."
        }, status=status.HTTP_201_CREATED)

    # 新規作成時の保存処理
    def perform_create(self, serializer):
        try:
            # NearMissの保存処理。ここでsaveメソッドが呼ばれ、nearMissNoが生成される
            near_miss = serializer.save()
            print(f"Successfully created NearMiss: {near_miss}")
            return near_miss  # nearMissオブジェクトを返す
        except Exception as e:
            print(f"Error during serializer.save(): {e}")
            raise e

    # 更新のためのメソッドを追加
    def update(self, request, *args, **kwargs):
        data = request.data
        company_code_str = data.get('companyCode')
        near_miss_no = data.get('nearMissNo')

        # companyCode と nearMissNo の両方が必要
        if not company_code_str or not near_miss_no:
            return Response(
                {"error": "companyCode and nearMissNo are required for update."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # NearMissオブジェクトを取得する
        try:
            near_miss = NearMiss.objects.get(companyCode__companyCode=company_code_str, nearMissNo=near_miss_no)
        except NearMiss.DoesNotExist:
            return Response(
                {"error": "NearMiss with given companyCode and nearMissNo not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # シリアライザを使って既存オブジェクトを更新
        serializer = self.get_serializer(near_miss, data=data, partial=True)  # partial=Trueで全フィールド更新しなくてもOKにする
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({
            "nearMissNo": near_miss.nearMissNo,
            "message": "NearMiss updated successfully."
        }, status=status.HTTP_200_OK)


    # 更新時の保存処理
    def perform_update(self, serializer):
        try:
            # NearMissの更新処理
            near_miss = serializer.save()
            print(f"Successfully updated NearMiss: {near_miss}")
        except Exception as e:
            print(f"Error during serializer.save(): {e}")
            raise e






# CompanyCode に基づく NearMiss の ViewSet
class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()  # CompanyCode の全データを対象にするクエリセット
    serializer_class = CompanyNearMissSerializer  # 使用するシリアライザを設定

    # クエリパラメータに基づいてフィルタリングされた NearMiss データを取得
    def get_queryset(self):
        company_code = self.request.query_params.get('companyCode', None)  # companyCode をクエリパラメータから取得
        queryset = CompanyCode.objects.prefetch_related('nearMiss_companyCode').all()  # 関連する NearMiss データをプリフェッチ
        if company_code:
            queryset = queryset.filter(companyCode=company_code)  # companyCode に基づいてフィルタリング
        return queryset



    # 新しいアクション：companyCode に対応する nearMissList の最後の nearMissNo を取得
    @action(detail=False, methods=['get'], url_path='last-near-miss-no')
    def get_last_near_miss_no(self, request):
        company_code = request.query_params.get('companyCode', None)
        if not company_code:
            return Response({"error": "companyCode is required."}, status=status.HTTP_400_BAD_REQUEST)

        # companyCode に一致するオブジェクトを取得
        try:
            company_obj = CompanyCode.objects.get(companyCode=company_code)
        except CompanyCode.DoesNotExist:
            return Response({"error": f"CompanyCode '{company_code}' does not exist."}, status=status.HTTP_404_NOT_FOUND)

        # companyCode に紐づく NearMissList を取得
        near_miss_list = NearMiss.objects.filter(companyCode=company_obj).order_by('-nearMissNo')

        if near_miss_list.exists():
            last_near_miss_no = near_miss_list.first().nearMissNo  # 最新の nearMissNo を取得
        else:
            last_near_miss_no = None  # 該当する nearMissList がない場合

        return Response({
            "lastNearMissNo": last_near_miss_no
        }, status=status.HTTP_200_OK)
    


    # companyCode と nearMissNo で NearMiss データを削除するためのアクション
    @action(detail=False, methods=['delete'], url_path='delete-by-code-and-no')
    def delete_by_code_and_no(self, request):
        company_code = request.query_params.get('companyCode')  # クエリパラメータから companyCode を取得
        near_miss_no = request.query_params.get('nearMissNo')  # クエリパラメータから nearMissNo を取得

        # companyCode または nearMissNo が存在しない場合はエラーレスポンスを返す
        if not company_code or not near_miss_no:
            return Response(
                {"error": "companyCode and nearMissNo are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # companyCode に一致するオブジェクトを取得
        try:
            company_code_obj = CompanyCode.objects.get(companyCode=company_code)
        except CompanyCode.DoesNotExist:
            # companyCode が存在しない場合、404エラーレスポンスを返す
            return Response(
                {"error": f"CompanyCode '{company_code}' does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        # companyCode と nearMissNo に一致する NearMiss を取得
        try:
            near_miss = NearMiss.objects.get(companyCode=company_code_obj, nearMissNo=near_miss_no)
        except NearMiss.DoesNotExist:
            # nearMissNo が存在しない場合、404エラーレスポンスを返す
            return Response(
                {"error": f"NearMiss with nearMissNo '{near_miss_no}' does not exist for companyCode '{company_code}'."},
                status=status.HTTP_404_NOT_FOUND
            )

        # NearMiss を削除
        near_miss.delete()
        return Response(
            {"message": f"NearMiss '{near_miss_no}' for companyCode '{company_code}' has been deleted."},
            status=status.HTTP_204_NO_CONTENT
        )
    





#----------------------------------------------------------------------------------------------------------------------------------------------









class SafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = SafetyIndicators.objects.all()
    serializer_class = SafetyIndicatorsSerializer


class CompanySafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanySafetyIndicatorsSerializer

    #クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('safetyIndicators_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






class TrendSafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = TrendSafetyIndicators.objects.all()
    serializer_class = TrendSafetyIndicatorsSerializer

class CompanyTrendSafetyIndicatorsViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyTrendSafetyIndicatorsSerializer

    def get_queryset(self):
        # Prefetch_related でソート順を指定
        prefetch = Prefetch(
            'trendSafetyIndicators_companyCode', 
            queryset=TrendSafetyIndicators.objects.order_by('lastUpdateDay')
        )
        queryset = CompanyCode.objects.prefetch_related(prefetch).all()
        
        # クエリパラメータでのフィルタリング
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset