from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import CompanyCode
from rest_framework.decorators import api_view
import numpy as np
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import (CalTablePlannedPM02,CalTableActualPM02,
                     CalTablePlannedPM03,CalTableActualPM03,
                     CalTableActualPM04,
                     CalTablePlannedPM05,CalTableActualPM05,
                     SummedPlannedCost,
                     SummedActualCost)

from .serializers import (CalTablePPM02Serializer,CalTableAPM02Serializer,
                          CompanyCodeCalPPM02Serializer,CompanyCodeCalAPM02Serializer,

                          CalTablePPM03Serializer,CalTableAPM03Serializer,
                          CompanyCodeCalPPM03Serializer,CompanyCodeCalAPM03Serializer,

                          CalTableAPM04Serializer,
                          CompanyCodeCalAPM04Serializer,

                          CalTablePPM05Serializer,CalTableAPM05Serializer,
                          CompanyCodeCalPPM05Serializer,CompanyCodeCalAPM05Serializer,

                          SummedPlannedCostSerializer,CompanyCodeSummedPlannedCostSerializer,
                          SummedActualCostSerializer,CompanyCodeSummedActualCostSerializer)


#PlannedPM02
class CalTablePPM02ViewSet(viewsets.ModelViewSet):
    queryset = CalTablePlannedPM02.objects.all()
    serializer_class = CalTablePPM02Serializer

class CompanyCodeCalTablePPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalPPM02Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTablePlannedPM02_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#ActualPM02
class CalTableAPM02ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM02.objects.all()
    serializer_class = CalTableAPM02Serializer

class CompanyCodeCalTableAPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM02Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM02_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#plannedPM03
class CalTablePPM03ViewSet(viewsets.ModelViewSet):
    queryset = CalTablePlannedPM03.objects.all()
    serializer_class = CalTablePPM03Serializer

class CompanyCodeCalTablePPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalPPM03Serializer

  
#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTablePlannedPM03_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#actualPM03
class CalTableAPM03ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM03.objects.all()
    serializer_class = CalTableAPM03Serializer

class CompanyCodeCalTableAPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM03Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM03_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#actualPM04
class CalTableAPM04ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM04.objects.all()
    serializer_class = CalTableAPM04Serializer

class CompanyCodeCalTableAPM04ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM04Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM04_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset





#plannedPM05
class CalTablePPM05ViewSet(viewsets.ModelViewSet):
    queryset = CalTablePlannedPM05.objects.all()
    serializer_class = CalTablePPM05Serializer

class CompanyCodeCalTablePPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalPPM05Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTablePlannedPM05_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset






#actualPM05
class CalTableAPM05ViewSet(viewsets.ModelViewSet):
    queryset = CalTableActualPM05.objects.all()
    serializer_class = CalTableAPM05Serializer

class CompanyCodeCalTableAPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeCalAPM05Serializer

#クエリパラメータでのフィルターリング
    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('calTableActualPM05_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    
    



# SummedPlannedCost
class SummedPlannedCostViewSet(viewsets.ModelViewSet):
    queryset = SummedPlannedCost.objects.all()
    serializer_class = SummedPlannedCostSerializer


class CompanyCodeSummedPlannedCostViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeSummedPlannedCostSerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('summedPlannedCost_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset


# SummedActualCost
class SummedActualCostViewSet(viewsets.ModelViewSet):
    queryset = SummedActualCost.objects.all()
    serializer_class = SummedActualCostSerializer


class CompanyCodeSummedActualCostViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeSummedActualCostSerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('summedActualCost_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset


@api_view(['GET'])
def calculate_errors(request):
    company_code = request.query_params.get('companyCode', None)
    year = request.query_params.get('year', None)
    
    print('Received companyCode:', company_code)
    print('Received year:', year)
    
    if not company_code or not year:
        print('Error: companyCode and year are required query parameters.')
        return Response({'error': 'companyCode and year are required query parameters.'}, status=400)
    
    try:
        year = int(year)
    except ValueError:
        print('Error: Year must be an integer.')
        return Response({'error': 'Year must be an integer.'}, status=400)

    try:
        company_code_obj = CompanyCode.objects.filter(companyCode=company_code).first()
        if not company_code_obj:
            print('Error: No company found with the specified companyCode.')
            return Response({'error': 'No company found with the specified companyCode.'}, status=404)

        planned_costs = SummedPlannedCost.objects.filter(companyCode=company_code_obj, year=year).first()
        actual_costs = SummedActualCost.objects.filter(companyCode=company_code_obj, year=year).first()

        if not planned_costs or not actual_costs:
            print('Error: No data found for the specified company code and year.')
            return Response({'error': 'No data found for the specified company code and year.'}, status=404)

        # デバッグ用のログ出力
        print(f"Planned Costs: {planned_costs}")
        print(f"Actual Costs: {actual_costs}")

        # 各月のデータを取得
        planned_values = [
            float(planned_costs.sumJan),
            float(planned_costs.sumFeb),
            float(planned_costs.sumMar),
            float(planned_costs.sumApr),
            float(planned_costs.sumMay),
            float(planned_costs.sumJun),
            float(planned_costs.sumJul),
            float(planned_costs.sumAug),
            float(planned_costs.sumSep),
            float(planned_costs.sumOct),
            float(planned_costs.sumNov),
            float(planned_costs.sumDec),
        ]

        actual_values = [
            float(actual_costs.sumJan),
            float(actual_costs.sumFeb),
            float(actual_costs.sumMar),
            float(actual_costs.sumApr),
            float(actual_costs.sumMay),
            float(actual_costs.sumJun),
            float(actual_costs.sumJul),
            float(actual_costs.sumAug),
            float(actual_costs.sumSep),
            float(actual_costs.sumOct),
            float(actual_costs.sumNov),
            float(actual_costs.sumDec),
        ]

        print(f"Planned Values: {planned_values}")
        print(f"Actual Values: {actual_values}")

        # 各月ごとの誤差指標を計算
        mae_list = []
        mse_list = []
        rmse_list = []
        mape_list = []

        for planned, actual in zip(planned_values, actual_values):
            mae = np.abs(planned - actual)
            mse = (planned - actual) ** 2
            rmse = np.sqrt(mse)
            mape = np.abs((planned - actual) / actual) * 100 if actual != 0 else 0

            mae_list.append(mae)
            mse_list.append(mse)
            rmse_list.append(rmse)
            mape_list.append(mape)

        print(f"MAE List: {mae_list}")
        print(f"MSE List: {mse_list}")
        print(f"RMSE List: {rmse_list}")
        print(f"MAPE List: {mape_list}")

        return Response({
            'MAE': mae_list,
            'MSE': mse_list,
            'RMSE': rmse_list,
            'MAPE': mape_list
        })
    except ValueError as e:
        print(f"ValueError during calculation: {e}")
        return Response({'error': f'ValueError during calculation: {e}'}, status=500)
    except TypeError as e:
        print(f"TypeError during calculation: {e}")
        return Response({'error': f'TypeError during calculation: {e}'}, status=500)
    except Exception as e:
        print(f"Error during calculation: {e}")
        return Response({'error': 'An error occurred during calculation.'}, status=500)