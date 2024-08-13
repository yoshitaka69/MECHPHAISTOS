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
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Reliability
from .serializers import CompanyReliabilitySerializer
from scipy.stats import norm, weibull_min
import numpy as np
import datetime
import pandas as pd


class CompanyCodeReliabilityViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyReliabilitySerializer
    queryset = CompanyCode.objects.all()

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('reliability_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset
    
    

    @action(detail=False, methods=['get'], url_path='weibull_distribution')
    def weibull_distribution(self, request):
        """
        Calculate Weibull distribution parameters and bathtub curve for reliability data associated with a company code.
        指定された会社コードに関連する信頼性データに対して、ワイブル分布のパラメータとバスタブ曲線を計算します。
        """
        company_code = request.query_params.get('companyCode', None)

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        data = []
        for reliability in reliability_entries:
            # Use MTBF as the scale parameter
            # Convert days to hours (1 day = 24 hours)
            scale_param = reliability.mtbf * 24 if reliability.mtbf is not None else 24

            if scale_param <= 0:
                continue  # Skip if MTBF is invalid

            # Set Weibull distribution parameters
            shape_params = [0.5, 1.0, 3.0]  # Early failure, random failure, wearout failure phases

            # Calculate failure rates for each phase
            x = np.linspace(0, 3000, 1000)  # Time axis
            pdf_initial = weibull_min.pdf(x, shape_params[0], scale=scale_param)
            pdf_random = weibull_min.pdf(x, shape_params[1], scale=scale_param)
            pdf_wearout = weibull_min.pdf(x, shape_params[2], scale=scale_param)

            # Fix invalid values in each array
            pdf_initial = np.nan_to_num(pdf_initial, nan=0.0, posinf=0.0, neginf=0.0)
            pdf_random = np.nan_to_num(pdf_random, nan=0.0, posinf=0.0, neginf=0.0)
            pdf_wearout = np.nan_to_num(pdf_wearout, nan=0.0, posinf=0.0, neginf=0.0)

            # Generate bathtub curve as total failure rate
            bathtub_curve = pdf_initial + pdf_random + pdf_wearout

            # Calculate the slope for wearout failure phase
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
                'slope': slope,  # Include slope
                'isWearoutIncreasing': is_wearout_increasing
            })

        if not data:
            return Response({'error': 'No valid MTBF data found'}, status=400)

        return Response(data)

    @action(detail=False, methods=['get'], url_path='reliability_parameters')
    def reliability_parameters(self, request):
        """
        Retrieve various reliability parameters and calculate impacts for each parameter.
        各パラメータに対して影響度を計算し、信頼性のパラメータを取得します。
        """
        company_code = request.query_params.get('companyCode', None)

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        parameter_data = []
        for reliability in reliability_entries:
            # Calculate impacts of parameters
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

    @action(detail=False, methods=['get'], url_path='bayesian_prediction')
    def bayesian_prediction(self, request):

        """
        Perform Bayesian prediction using reliability data to estimate future failures.
        信頼性データを使用して将来の故障を推定するベイジアン予測を行います。
        """

        company_code = request.query_params.get('companyCode', None)
        window_size = int(request.query_params.get('windowSize', 365))  # Sliding window size (days)
        step_size = int(request.query_params.get('stepSize', 30))  # Sliding window step size (days)

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        predictions = []
        today = datetime.date.today()
        for entry in reliability_entries:
            # Set default values if necessary parameters are None
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
                # Set prior distribution mean
                prior_mean = mtbf * (1 - 0.1 * failure_type)

                # Set prior distribution standard deviation
                prior_std = mttr / 2 * (1 + 0.1 * maintenance_impact)

                # Set likelihood mean
                likelihood_mean = mttf * (1 + 0.05 * maintenance_frequency)

                # Set likelihood standard deviation
                likelihood_std = mttr / 2 * (1 - 0.1 * environment_condition)

                # Calculate posterior distribution mean
                posterior_mean = (prior_mean + likelihood_mean) / 2

                # Calculate posterior distribution standard deviation
                posterior_std = (prior_std + likelihood_std) / 2

                               # Set x-axis range for failure prediction
                x = np.linspace(0, 1000, 100)

                # Calculate the probability density function for the posterior distribution
                posterior_pdf = norm.pdf(x, posterior_mean, posterior_std)

                predictions.append({
                    'machineName': entry.machineName.machineName if entry.machineName else '',
                    'x': x.tolist(),
                    'posterior_pdf': posterior_pdf.tolist(),
                    'mttr': mttr,
                    'start_date': start_date,
                    'end_date': end_date,
                })

                # Advance the window by step size
                start_date += datetime.timedelta(days=step_size)
                end_date += datetime.timedelta(days=step_size)

        return Response(predictions)






    @action(detail=False, methods=['get'], url_path='correlation')
    def correlation_matrix(self, request):
        company_code = request.query_params.get('companyCode', None)
        if not company_code:
            return Response({"error": "companyCode is required"}, status=400)

        company = CompanyCode.objects.prefetch_related('reliability_companyCode').filter(companyCode=company_code).first()
        if not company:
            return Response({"error": "Company code not found"}, status=404)

        reliability_data = company.reliability_companyCode.all().values('mttr', 'mtbf', 'mttf', 'totalOperatingTime', 'failureCount')
        reliability_list = list(reliability_data)
        if not reliability_list:
            return Response({"error": "No reliability data found"}, status=404)

        # データフレームに変換
        df = pd.DataFrame(reliability_list)
        df = df[['mttr', 'mtbf', 'mttf', 'totalOperatingTime', 'failureCount']]

        # 無限大やNaNを処理
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.fillna(0, inplace=True)

        # 相関行列の計算
        correlation_matrix = df.corr().to_dict()

        return Response(correlation_matrix)



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






