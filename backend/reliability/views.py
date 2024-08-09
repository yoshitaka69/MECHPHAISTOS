from rest_framework import viewsets
from .models import FailurePredictionPoint
from .serializers import FPPSerializer,CompanyFPPSerializer
from django.http import JsonResponse
import numpy as np




#ReliabilityのviewSet
#------------------------------------------------------------------------------------------------------------------------

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reliability, CompanyCode
from .serializers import ReliabilitySerializer, CompanyReliabilitySerializer
from scipy.stats import weibull_min
import numpy as np

class ReliabilityViewSet(viewsets.ModelViewSet):
    queryset = Reliability.objects.all()
    serializer_class = ReliabilitySerializer






from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reliability
from scipy.stats import norm
import numpy as np
import datetime

class CompanyCodeReliabilityViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyReliabilitySerializer

    def get_queryset(self):
        queryset = Reliability.objects.all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode__companyCode=company_code)
        return queryset

    @action(detail=False, methods=['get'], url_path='weibull_distribution')
    def weibull_distribution(self, request):
        company_code = request.query_params.get('companyCode', None)

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        data = []
        for reliability in reliability_entries:
            # MTBFを尺度パラメータとして使用
            # モデルでは日数で保存されているため、時間に変換する（1日=24時間）
            scale_param = reliability.mtbf * 24 if reliability.mtbf is not None else 24

            if scale_param <= 0:
                continue  # MTBFが無効な場合はスキップ

            # ワイブル分布のパラメータ設定
            shape_params = [0.5, 1.0, 3.0]  # 初期故障期, 偶発故障期, 磨耗故障期

            # 各フェーズに対応する故障率の計算
            x = np.linspace(0, 3000, 1000)  # 時間軸
            pdf_initial = weibull_min.pdf(x, shape_params[0], scale=scale_param)
            pdf_random = weibull_min.pdf(x, shape_params[1], scale=scale_param)
            pdf_wearout = weibull_min.pdf(x, shape_params[2], scale=scale_param)

            # 各配列の無効な値を修正
            pdf_initial = np.nan_to_num(pdf_initial, nan=0.0, posinf=0.0, neginf=0.0)
            pdf_random = np.nan_to_num(pdf_random, nan=0.0, posinf=0.0, neginf=0.0)
            pdf_wearout = np.nan_to_num(pdf_wearout, nan=0.0, posinf=0.0, neginf=0.0)

            # 合計故障率としてバスタブ曲線の生成
            bathtub_curve = pdf_initial + pdf_random + pdf_wearout

            # 摩耗故障期の傾きの計算
            wearout_start_index = len(x) * 2 // 3
            wearout_end_index = len(x) - 1
            slope = bathtub_curve[wearout_end_index] - bathtub_curve[wearout_start_index]
            is_wearout_increasing = slope > 0

            data.append({
                'reliability_id': reliability.id,
                'times': x.tolist(),
                'pdf_initial': pdf_initial.tolist(),
                'pdf_random': pdf_random.tolist(),
                'pdf_wearout': pdf_wearout.tolist(),
                'bathtub_curve': bathtub_curve.tolist(),
                'slope': slope,  # 傾きを追加
                'isWearoutIncreasing': is_wearout_increasing
            })

        if not data:
            return Response({'error': 'No valid MTBF data found'}, status=400)

        return Response(data)

    @action(detail=False, methods=['get'], url_path='reliability_parameters')
    def reliability_parameters(self, request):
        company_code = request.query_params.get('companyCode', None)

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        parameter_data = []
        for reliability in reliability_entries:
            # バスタブ曲線の計算を再利用するため、再度計算
            scale_param = reliability.mtbf * 24 if reliability.mtbf is not None else 24
            x = np.linspace(0, 3000, 1000)
            pdf_initial = weibull_min.pdf(x, 0.5, scale=scale_param)
            pdf_random = weibull_min.pdf(x, 1.0, scale=scale_param)
            pdf_wearout = weibull_min.pdf(x, 3.0, scale=scale_param)
            bathtub_curve = pdf_initial + pdf_random + pdf_wearout
            wearout_start_index = len(x) * 2 // 3
            wearout_end_index = len(x) - 1
            slope = bathtub_curve[wearout_end_index] - bathtub_curve[wearout_start_index]

            parameter_data.append({
                'companyCode': reliability.companyCode.companyCode,
                'ceListNo': reliability.ceListNo.id if reliability.ceListNo else None,
                'mttr': reliability.mttr,
                'mtbf': reliability.mtbf,
                'mttf': reliability.mttf,
                'totalOperatingTime': reliability.totalOperatingTime,
                'failureCount': reliability.failureCount,
                'slope': slope,  # 傾きを追加
                'isWearoutIncreasing': slope > 0
            })

        return Response(parameter_data)

    @action(detail=False, methods=['get'], url_path='bayesian_prediction')
    def bayesian_prediction(self, request):
        company_code = request.query_params.get('companyCode', None)
        window_size = int(request.query_params.get('windowSize', 365))  # スライディングウィンドウのサイズ（日数）
        step_size = int(request.query_params.get('stepSize', 30))  # スライディングウィンドウのステップサイズ（日数）

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        predictions = []
        today = datetime.date.today()
        for entry in reliability_entries:
            # 必要なパラメータがNoneの場合、デフォルト値を設定
            mtbf = entry.mtbf if entry.mtbf is not None else 1
            mttr = entry.mttr if entry.mttr is not None else 1
            mttf = entry.mttf if entry.mttf is not None else 1
            failure_type = entry.failureType if entry.failureType is not None else 0
            maintenance_impact = entry.maintenanceImpact if entry.maintenanceImpact is not None else 0
            maintenance_frequency = entry.maintenanceFrequency if entry.maintenanceFrequency is not None else 0
            environment_condition = entry.environmentCondition if entry.environmentCondition is not None else 0

            start_date = today - datetime.timedelta(days=window_size)
            end_date = start_date + datetime.timedelta(days=window_size)
            while end_date <= today:
                # 事前分布の平均を設定
                prior_mean = mtbf * (1 - 0.1 * failure_type)

                # 事前分布の標準偏差を設定
                prior_std = mttr / 2 * (1 + 0.1 * maintenance_impact)

                # 尤度の平均を設定
                likelihood_mean = mttf * (1 + 0.05 * maintenance_frequency)

                # 尤度の標準偏差を設定
                likelihood_std = mttr / 2 * (1 - 0.1 * environment_condition)

                # 事後分布の平均を計算
                posterior_mean = (prior_mean + likelihood_mean) / 2

                # 事後分布の標準偏差を計算
                posterior_std = (prior_std + likelihood_std) / 2

                # 故障予測のためのx軸の範囲を設定
                x = np.linspace(0, 1000, 100)

                # 事後分布の確率密度関数を計算
                posterior_pdf = norm.pdf(x, posterior_mean, posterior_std)

                predictions.append({
                    'machineName': entry.machineName.machineName if entry.machineName else '',
                    'x': x.tolist(),
                    'posterior_pdf': posterior_pdf.tolist(),
                    'mttr': mttr,
                    'start_date': start_date,
                    'end_date': end_date,
                })

                # ウィンドウをステップサイズ分進める
                start_date += datetime.timedelta(days=step_size)
                end_date += datetime.timedelta(days=step_size)

        return Response(predictions)
    


    @action(detail=False, methods=['get'], url_path='reliability_parameters')
    def reliability_parameters(self, request):
        company_code = request.query_params.get('companyCode', None)

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        parameter_data = []
        for reliability in reliability_entries:
            # パラメータの影響度を計算
            failure_type_impact = reliability.failureType * 10 if reliability.failureType else 0
            maintenance_method_impact = reliability.maintenanceMethod * 5 if reliability.maintenanceMethod else 0
            failure_cause_impact = reliability.failureCause * 7 if reliability.failureCause else 0
            environmental_impact = reliability.environmentCondition * 3 if reliability.environmentCondition else 0
            operational_impact = reliability.operationalCondition * 2 if reliability.operationalCondition else 0
            component_condition_impact = reliability.componentCondition * 4 if reliability.componentCondition else 0

            parameter_data.append({
                'companyCode': reliability.companyCode.companyCode,
                'ceListNo': reliability.ceListNo.id if reliability.ceListNo else None,
                'mttr': reliability.mttr,
                'mtbf': reliability.mtbf,
                'mttf': reliability.mttf,
                'totalOperatingTime': reliability.totalOperatingTime,
                'failureCount': reliability.failureCount,
                'failureType': reliability.failureType,
                'failureTypeImpact': failure_type_impact,
                'failureMode': reliability.failureMode,
                'maintenanceMethod': reliability.maintenanceMethod,
                'maintenanceMethodImpact': maintenance_method_impact,
                'maintenanceFrequency': reliability.maintenanceFrequency,
                'maintenanceImpact': reliability.maintenanceImpact,
                'failureCause': reliability.failureCause,
                'failureCauseImpact': failure_cause_impact,
                'environmentCondition': reliability.environmentCondition,
                'environmentConditionImpact': environmental_impact,
                'operationalCondition': reliability.operationalCondition,
                'operationalConditionImpact': operational_impact,
                'componentCondition': reliability.componentCondition,
                'componentConditionImpact': component_condition_impact,
            })

        return Response(parameter_data)





#------------------------------------------------------------------------------------------------------------------------








#TroubleHistoryのviewSet
#------------------------------------------------------------------------------------------------------------------------

from rest_framework import viewsets
from .models import CompanyCode, TroubleHistory
from .serializers import TroubleHistorySerializer,CompanyTroubleHistorySerializer


class TroubleHistoryViewSet(viewsets.ModelViewSet):
    queryset = TroubleHistory.objects.all()
    serializer_class = TroubleHistorySerializer

class CompanyCodeTroubleHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTroubleHistorySerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('troubleHistory_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
#------------------------------------------------------------------------------------------------------------------------





#FailurePredictionPointのviewSet
#------------------------------------------------------------------------------------------------------------------------
class FailurePredictionPointViewSet(viewsets.ModelViewSet):
    queryset = FailurePredictionPoint.objects.all()
    serializer_class = FPPSerializer

class CompanyCodeFPPViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyFPPSerializer

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('failurePredictionPoint_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
#------------------------------------------------------------------------------------------------------------------------






