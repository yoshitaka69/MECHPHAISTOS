from rest_framework import viewsets
from .models import FailureData, WeibullData,FailurePredictionPoint
from .serializers import FailureDataSerializer, WeibullDataSerializer,FPPSerializer,CompanyFPPSerializer
from django.http import JsonResponse
import numpy as np





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








# FailureDataモデルのビューセット
class FailureDataViewSet(viewsets.ModelViewSet):
    queryset = FailureData.objects.all()  # すべてのFailureDataインスタンスをクエリ
    serializer_class = FailureDataSerializer  # 使用するシリアライザー

# 故障予測を行うビュー
#def predict_failure(request):
    # 1月から12月までの月を表す配列
   # months = np.arange(1, 13)
    # 各月に対応するランダムな故障発生確率の配列を生成
    #probabilities = np.random.rand(12)
    # JSON形式でレスポンスを返す
    #return JsonResponse({
        #'months': months.tolist(),  # 月の配列をリストに変換
        #'probabilities': probabilities.tolist(),  # 確率の配列をリストに変換
    #})





#ワイブルデータ
class WeibullDataViewSet(viewsets.ModelViewSet):
    queryset = WeibullData.objects.all()
    serializer_class = WeibullDataSerializer




#------------------------------------------------------------------------------------------------------------------
import logging
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from scipy.ndimage import uniform_filter1d
from sklearn.ensemble import RandomForestClassifier
from .models import BayesianPrediction
from .serializers import BayesianPredictionSerializer

logger = logging.getLogger(__name__)

class BayesianPredictionViewSet(viewsets.ModelViewSet):
    queryset = BayesianPrediction.objects.all()
    serializer_class = BayesianPredictionSerializer

@api_view(['POST'])
def predict_failure(request):
    try:
        logger.debug(f"Request data: {request.data}")

        data = request.data
        times = list(map(int, data.get('times', [])))
        failures = list(map(int, data.get('failures', [])))
        failure_types = data.get('failure_types', [])
        failure_causes = data.get('failure_causes', [])
        maintenance_types = data.get('maintenance_types', [])
        maintenance_results = data.get('maintenance_results', [])
        window_size = int(data.get('window_size', 3))

        if len(times) < 2 or len(failures) < 2:
            raise ValueError("Insufficient data for prediction. Please provide more data points.")

        # ラベルエンコーディング
        label_encoder_failure_type = LabelEncoder()
        label_encoder_failure_cause = LabelEncoder()
        label_encoder_maintenance_type = LabelEncoder()
        label_encoder_maintenance_result = LabelEncoder()

        failure_types_encoded = label_encoder_failure_type.fit_transform(failure_types)
        failure_causes_encoded = label_encoder_failure_cause.fit_transform(failure_causes)
        maintenance_types_encoded = label_encoder_maintenance_type.fit_transform(maintenance_types)
        maintenance_results_encoded = label_encoder_maintenance_result.fit_transform(maintenance_results)

        # ワンホットエンコーディング
        onehot_encoder = OneHotEncoder(sparse_output=False)
        failure_types_onehot = onehot_encoder.fit_transform(np.array(failure_types_encoded).reshape(-1, 1))
        failure_causes_onehot = onehot_encoder.fit_transform(np.array(failure_causes_encoded).reshape(-1, 1))
        maintenance_types_onehot = onehot_encoder.fit_transform(np.array(maintenance_types_encoded).reshape(-1, 1))
        maintenance_results_onehot = onehot_encoder.fit_transform(np.array(maintenance_results_encoded).reshape(-1, 1))

        # ベイズ更新と予測故障率の計算
        posterior_alphas = []
        posterior_betas = []
        predicted_failure_rates = []

        prior_alpha = 1
        prior_beta = 1

        for t, f, ft, fc, mt, mr in zip(times, failures, failure_types_onehot, failure_causes_onehot, maintenance_types_onehot, maintenance_results_onehot):
            # エンコーディングされたデータの影響を加味してベイズ更新を行う
            influence = np.mean(ft) + np.mean(fc) + np.mean(mt) + np.mean(mr)
            adjusted_failure_count = f + influence

            posterior_alpha = prior_alpha + adjusted_failure_count
            posterior_beta = prior_beta + t
            posterior_alphas.append(posterior_alpha)
            posterior_betas.append(posterior_beta)

            predicted_failure_rate = posterior_alpha / posterior_beta
            predicted_failure_rates.append(predicted_failure_rate)

        smoothed_rates = uniform_filter1d(predicted_failure_rates, size=window_size)
        rate_changes = np.diff(smoothed_rates)

        logger.debug(f"Smoothed rates: {smoothed_rates}")
        logger.debug(f"Rate changes: {rate_changes}")

        if len(smoothed_rates) <= 1 or len(rate_changes) == 0:
            raise ValueError("Insufficient data for prediction")

        labels = np.array([0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])
        if len(smoothed_rates) - 1 != len(rate_changes):
            raise ValueError("Inconsistent sample numbers between smoothed rates and rate changes")
        X = np.column_stack((smoothed_rates[:-1], rate_changes))
        y = labels[1:len(X)+1]

        logger.debug(f"Training data X: {X}, y: {y}")

        model = RandomForestClassifier()
        model.fit(X, y)
        predicted_phases = model.predict(X)

        return JsonResponse({
            'times': times,
            'predicted_failure_rates': predicted_failure_rates,
            'rate_changes': rate_changes.tolist(),
            'predicted_phases': predicted_phases.tolist()
        })
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return JsonResponse({'error': str(e)}, status=500)


#------------------------------------------------------------------------------------------------------------------