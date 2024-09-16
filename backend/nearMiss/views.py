from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from .models import (
    NearMiss, 
    CompanyCode, 
    SafetyIndicators, 
    TrendSafetyIndicators, 
    CustomUser
)

from .serializers import (
    NearMissSerializer, 
    CompanyNearMissSerializer,
    SafetyIndicatorsSerializer, 
    CompanySafetyIndicatorsSerializer,
    TrendSafetyIndicatorsSerializer, 
    CompanyTrendSafetyIndicatorsSerializer
)



#----------------------------------------------------------------------------------------------------------------------------------------------

class NearMissViewSet(viewsets.ModelViewSet):
    queryset = NearMiss.objects.all()
    serializer_class = NearMissSerializer

@api_view(['POST'])
def create_near_miss(request):
    if request.method == 'POST':
        serializer = NearMissSerializer(data=request.data)
        if serializer.is_valid():
            near_miss = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CompanyCode, NearMiss
from .serializers import CompanyNearMissSerializer, NearMissSerializer

# ログを設定
logger = logging.getLogger(__name__)

class CompanyNearMissViewSet(viewsets.ModelViewSet):
    queryset = CompanyCode.objects.all()
    serializer_class = CompanyNearMissSerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('nearMiss_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset

    def create(self, request, *args, **kwargs):
        company_code_value = request.data.get('companyCode')

        # companyCode が存在するかチェック
        if not company_code_value:
            logger.error('Error: companyCode is missing from request data.')
            return Response({'error': 'Company code is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # companyCode の取得
            company_code = CompanyCode.objects.get(companyCode=company_code_value)
            logger.info(f'Company code found: {company_code}')
        except CompanyCode.DoesNotExist:
            logger.error(f'Error: Invalid company code {company_code_value}')
            return Response({'error': f'Invalid company code: {company_code_value}'}, status=status.HTTP_400_BAD_REQUEST)

        # NearMissNo の生成ロジック
        existing_near_miss_nos = NearMiss.objects.filter(companyCode=company_code).values_list('nearMissNo', flat=True).order_by('nearMissNo')
        logger.debug(f'Existing NearMissNos: {list(existing_near_miss_nos)}')

        # 使用されている番号のセットを作成
        used_numbers = set(int(nm.split('-')[-1]) for nm in existing_near_miss_nos if nm.split('-')[-1].isdigit())
        logger.debug(f'Used numbers: {used_numbers}')

        # 未使用の番号を探す
        new_number = None
        for i in range(1, len(used_numbers) + 2):
            if i not in used_numbers:
                new_number = i
                break

        # 最大の番号に +1 する
        if new_number is None:
            new_number = max(used_numbers) + 1 if used_numbers else 1
        logger.info(f'New number generated: {new_number}')

        # NearMissNo をフォーマット
        near_miss_no = f"NearMissNo-{str(new_number).zfill(5)}"
        logger.info(f'Generated NearMissNo: {near_miss_no}')

        # データのコピー
        near_miss_data = request.data.copy()
        near_miss_data['companyCode'] = company_code_value
        near_miss_data['nearMissNo'] = near_miss_no  # 生成した NearMissNo を設定

        # シリアライズして保存
        serializer = NearMissSerializer(data=near_miss_data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Data successfully saved.')
            return Response({
                'data': serializer.data,
                'lastNearMissNo': near_miss_no  # NearMissNo をレスポンスに含める
            }, status=status.HTTP_201_CREATED)
        else:
            logger.error(f'Serializer validation failed: {serializer.errors}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






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
