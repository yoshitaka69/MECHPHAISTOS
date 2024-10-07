from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.http import JsonResponse

# モデルとシリアライザー
from .models import Reliability, CompanyCode, FailurePredictionPoint
from .serializers import (
    CompanyReliabilitySerializer, 
    ReliabilitySerializer, 
    FPPSerializer, 
    CompanyFPPSerializer
)

# サードパーティライブラリ
from scipy.stats import norm, weibull_min
import numpy as np
import pandas as pd
import datetime

# 機械学習関連
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import shap





#ReliabilityのviewSet
#------------------------------------------------------------------------------------------------------------------------
class ReliabilityViewSet(viewsets.ModelViewSet):
    queryset = Reliability.objects.all()
    serializer_class = ReliabilitySerializer


class CompanyCodeReliabilityViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyReliabilitySerializer
    queryset = CompanyCode.objects.all()

    def get_queryset(self):
        queryset = CompanyCode.objects.prefetch_related('reliability_companyCode').all()
        company_code = self.request.query_params.get('companyCode', None)
        if company_code:
            queryset = queryset.filter(companyCode=company_code)
        return queryset

    # 信頼性のパラメータを取得
    @action(detail=False, methods=['get'], url_path='reliability_parameters')
    def reliability_parameters(self, request):
        """
        Retrieve various reliability parameters and calculate impacts for each parameter.
        各パラメータに対して影響度を計算し、信頼性のパラメータを取得します。
        """
        # クエリパラメータから会社コードを取得
        company_code = request.query_params.get('companyCode', None)

        # 会社コードが提供されていない場合はエラーレスポンスを返す
        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        # 会社コードに関連する信頼性エントリをデータベースから取得
        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        # 該当する信頼性エントリがない場合、エラーレスポンスを返す
        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        # 各信頼性エントリのパラメータデータを格納するリスト
        parameter_data = []

        # 信頼性エントリをループし、それぞれの影響度を計算してデータに追加
        for reliability in reliability_entries:
            # 各パラメータの影響度を計算
            failure_type_impact = reliability.failureType * 10 if reliability.failureType else 0
            maintenance_method_impact = reliability.maintenanceMethod * 5 if reliability.maintenanceMethod else 0
            failure_cause_impact = reliability.failureCause * 7 if reliability.failureCause else 0
            operational_impact = reliability.operationalCondition * 2 if reliability.operationalCondition else 0
            component_condition_impact = reliability.componentCondition * 4 if reliability.componentCondition else 0
            pm_type_impact = 1  # PMTypeの影響度は1とする

            # 各エントリのパラメータを辞書形式でリストに追加
            parameter_data.append({
                'companyCode': reliability.companyCode.companyCode,  # 会社コード
                'ceListNo': reliability.ceListNo.id if reliability.ceListNo else None,  # CEリスト番号
                'mttr': reliability.mttr,  # MTTR（平均修理時間）
                'mtbf': reliability.mtbf,  # MTBF（平均故障間隔）
                'mttf': reliability.mttf,  # MTTF（平均故障時間）
                'totalOperatingTime': reliability.totalOperatingTime,  # 総稼働時間
                'failureCount': reliability.failureCount,  # 故障回数
                'failureType': reliability.failureType,  # 故障タイプ
                'failureTypeImpact': failure_type_impact,  # 故障タイプの影響度
                'failureMode': reliability.failureMode,  # 故障モード
                'maintenanceMethod': reliability.maintenanceMethod,  # 保全方法
                'maintenanceMethodImpact': maintenance_method_impact,  # 保全方法の影響度
                'maintenanceFrequency': reliability.maintenanceFrequency,  # 保全頻度
                'maintenanceImpact': reliability.maintenanceImpact,  # 保全の影響
                'failureCause': reliability.failureCause,  # 故障原因
                'failureCauseImpact': failure_cause_impact,  # 故障原因の影響度
                'operationalCondition': reliability.operationalCondition,  # 運転状態
                'operationalConditionImpact': operational_impact,  # 運転状態の影響度
                'componentCondition': reliability.componentCondition,  # 部品状態
                'componentConditionImpact': component_condition_impact,  # 部品状態の影響度
                'PMType': reliability.PMType,  # PMタイプ
                'PMTypeImpact': pm_type_impact  # PMタイプの影響度は1
            })

        # 最終的に計算されたパラメータデータをレスポンスとして返す
        return Response(parameter_data)

    # 相関行列のヒートマップ
    @action(detail=False, methods=['get'], url_path='correlation')
    def get_heatmap_data(self, request):
        """
        Calculate the correlation matrix of various reliability factors and return the data for heatmap visualization.
        信頼性要因の相関行列を計算し、ヒートマップのデータを返します。
        """
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  
                    "MTBF": reliability.mtbf,  
                    "MTTF": reliability.mttf,  
                    "failureCount": reliability.failureCount,  
                    "totalOperatingTime": reliability.totalOperatingTime,  
                    "failureType": reliability.failureType,  
                    "failureMode": reliability.failureMode,  
                    "maintenanceMethod": reliability.maintenanceMethod,  
                    "maintenanceFrequency": reliability.maintenanceFrequency,  
                    "PMType": reliability.PMType,  
                    "failureCause": reliability.failureCause,  
                    "operationalCondition": reliability.operationalCondition,  
                    "componentCondition": reliability.componentCondition  
                })

            df = pd.DataFrame(data)
            correlation_matrix = df.corr().replace([np.inf, -np.inf], np.nan).fillna(0).round(2)
            heatmap_data = correlation_matrix.reset_index().melt(id_vars=['index'])
            heatmap_data.columns = ['x', 'y', 'value']

            return Response(heatmap_data.to_dict(orient='records'))

        except Exception as e:
            return Response({"error": "An error occurred while processing the request."}, status=500)

    # ランダムフォレストによる特徴量の重要度
    @action(detail=False, methods=['get'], url_path='feature_importance_details')
    def get_feature_importance_details(self, request):
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  
                    "MTBF": reliability.mtbf,  
                    "MTTF": reliability.mttf,  
                    "failureCount": reliability.failureCount,  
                    "totalOperatingTime": reliability.totalOperatingTime,  
                    "failureType": reliability.failureType,  
                    "failureMode": reliability.failureMode,  
                    "maintenanceMethod": reliability.maintenanceMethod,  
                    "maintenanceFrequency": reliability.maintenanceFrequency,  
                    "PMType": reliability.PMType,  
                    "failureCause": reliability.failureCause,  
                    "operationalCondition": reliability.operationalCondition,  
                    "componentCondition": reliability.componentCondition  
                })

            df = pd.DataFrame(data)
            X = df.drop(columns=['failureCount'])
            y = df['failureCount']
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X, y)
            importance = model.feature_importances_
            feature_importance = [{"feature": f, "importance": round(imp, 2)} for f, imp in zip(X.columns, importance)]

            return Response({
                "feature_importance": feature_importance
            })

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)

    # ベイズ予測
    @action(detail=False, methods=['get'], url_path='bayesian_prediction')
    def bayesian_prediction(self, request):
        company_code = request.query_params.get('companyCode', None)
        window_size = int(request.query_params.get('windowSize', 365))
        step_size = int(request.query_params.get('stepSize', 30))

        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        predictions = []
        today = datetime.date.today()

        for reliability in reliability_entries:
            mtbf = reliability.mtbf if reliability.mtbf is not None else 1
            mttr = reliability.mttr if reliability.mttr is not None else 1
            mttf = reliability.mttf if reliability.mttf is not None else 1
            failure_type = reliability.failureType if reliability.failureType is not None else 0
            failure_mode = reliability.failureMode if reliability.failureMode is not None else 0
            maintenance_method = reliability.maintenanceMethod if reliability.maintenanceMethod is not None else 0
            maintenance_impact = reliability.maintenanceImpact if reliability.maintenanceImpact is not None else 0
            maintenance_frequency = reliability.maintenanceFrequency if reliability.maintenanceFrequency is not None else 0
            failure_cause = reliability.failureCause if reliability.failureCause is not None else 0
            operational_condition = reliability.operationalCondition if reliability.operationalCondition is not None else 0
            component_condition = reliability.componentCondition if reliability.componentCondition is not None else 0
            pm_type = reliability.PMType if reliability.PMType is not None else 0

            start_date = today - datetime.timedelta(days=window_size)
            end_date = start_date + datetime.timedelta(days=window_size)

            while end_date <= today:
                prior_mean = mtbf * (1 - 0.1 * failure_type)
                prior_std = mttr / 2 * (1 + 0.1 * maintenance_impact)
                likelihood_mean = mttf * (1 + 0.05 * maintenance_frequency)
                likelihood_std = mttr / 2
                posterior_mean = (prior_mean + likelihood_mean) / 2
                posterior_std = (prior_std + likelihood_std) / 2

                x = np.linspace(0, 1000, 100)
                posterior_pdf = norm.pdf(x, posterior_mean, posterior_std)

                predictions.append({
                    'companyCode': reliability.companyCode.companyCode,
                    'ceListNo': reliability.ceListNo.id if reliability.ceListNo else None,
                    'mttr': mttr,
                    'mtbf': mtbf,
                    'mttf': mttf,
                    'totalOperatingTime': reliability.totalOperatingTime,
                    'failureCount': reliability.failureCount,
                    'failureType': failure_type,
                    'failureTypeImpact': failure_type * 10,
                    'failureMode': failure_mode,
                    'maintenanceMethod': maintenance_method,
                    'maintenanceMethodImpact': maintenance_method * 5,
                    'maintenanceFrequency': maintenance_frequency,
                    'maintenanceImpact': maintenance_impact,
                    'failureCause': failure_cause,
                    'failureCauseImpact': failure_cause * 7,
                    'operationalCondition': operational_condition,
                    'operationalConditionImpact': operational_condition * 2,
                    'componentCondition': component_condition,
                    'componentConditionImpact': component_condition * 4,
                    'PMType': pm_type,
                    'PMTypeImpact': 1,
                    'x': x.tolist(),
                    'posterior_pdf': posterior_pdf.tolist(),
                    'start_date': start_date,
                    'end_date': end_date,
                })

                start_date += datetime.timedelta(days=step_size)
                end_date += datetime.timedelta(days=step_size)

        return Response(predictions)

    # 回帰分析
    @action(detail=False, methods=['get'], url_path='regression_analysis')
    def get_regression_analysis(self, request):
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  
                    "MTBF": reliability.mtbf,  
                    "MTTF": reliability.mttf,  
                    "failureCount": reliability.failureCount,  
                    "totalOperatingTime": reliability.totalOperatingTime,  
                    "failureType": reliability.failureType,  
                    "failureMode": reliability.failureMode,  
                    "maintenanceMethod": reliability.maintenanceMethod,  
                    "maintenanceFrequency": reliability.maintenanceFrequency,  
                    "failureCause": reliability.failureCause,  
                    "operationalCondition": reliability.operationalCondition,  
                    "componentCondition": reliability.componentCondition,  
                    "PMType": reliability.PMType  
                })

            df = pd.DataFrame(data)
            features = df.columns.drop('MTTF')
            regression_results = {}

            for feature in features:
                X = df[[feature]].fillna(0)
                y = df['MTTF'].fillna(0)
                model = LinearRegression()
                model.fit(X, y)

                slope = model.coef_[0]
                intercept = model.intercept_
                y_pred = model.predict(X)
                n = len(X)
                mean_x = np.mean(X[feature])
                t_value = 1.96
                se = np.sqrt(np.sum((y - y_pred) ** 2) / (n - 2))
                se_line = se * np.sqrt(1 / n + (X[feature] - mean_x) ** 2 / np.sum((X[feature] - mean_x) ** 2))

                lower_bound = y_pred - t_value * se_line
                upper_bound = y_pred + t_value * se_line

                lower_bound = np.nan_to_num(lower_bound, nan=0.0, posinf=0.0, neginf=0.0)
                upper_bound = np.nan_to_num(upper_bound, nan=0.0, posinf=0.0, neginf=0.0)

                regression_results[feature] = {
                    "slope": round(slope, 2),
                    "intercept": round(intercept, 2),
                    "points": [[x, round(slope * x + intercept, 2)] for x in X[feature]],
                    "confidence_interval": {
                        "lower": lower_bound.tolist(),
                        "upper": upper_bound.tolist()
                    }
                }

            return Response(regression_results)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)

    # SHAP値の取得
    @action(detail=False, methods=['get'], url_path='shap_values') 
    def get_shap_values(self, request):
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  
                    "MTBF": reliability.mtbf,  
                    "MTTF": reliability.mttf,  
                    "failureCount": reliability.failureCount,  
                    "totalOperatingTime": reliability.totalOperatingTime,  
                    "failureType": reliability.failureType,  
                    "failureMode": reliability.failureMode,  
                    "maintenanceMethod": reliability.maintenanceMethod,  
                    "maintenanceFrequency": reliability.maintenanceFrequency,  
                    "failureCause": reliability.failureCause,  
                    "operationalCondition": reliability.operationalCondition,  
                    "componentCondition": reliability.componentCondition,  
                    "PMType": reliability.PMType  
                })

            df = pd.DataFrame(data)
            features = df.columns
            X = df.fillna(0)
            model = RandomForestRegressor()
            model.fit(X, X["failureCount"])
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X)

            shap_data = []
            for i in range(len(shap_values)):
                shap_data.append({feature: shap_values[i][j] for j, feature in enumerate(features)})

            return Response({"shap_values": shap_data, "features": features.tolist()})

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)

    # PCAの実行
    @action(detail=False, methods=['get'], url_path='pca')
    def perform_pca(self, request):
        company_code = request.query_params.get('companyCode')

        company = CompanyCode.objects.filter(companyCode=company_code).first()

        if not company:
            return Response({"error": "Company code not found."}, status=404)

        queryset = Reliability.objects.filter(companyCode=company)
        data = queryset.values(
            'mttr', 'mtbf', 'mttf', 'failureCount', 'totalOperatingTime', 
            'failureType', 'failureMode', 'maintenanceMethod', 'maintenanceFrequency', 
            'failureCause', 'operationalCondition', 'componentCondition', 'PMType'
        )

        df = pd.DataFrame(list(data))
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(df.fillna(0))
        pca_scores = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
        explained_variance = pca.explained_variance_ratio_

        return Response({
            'pca_scores': pca_scores.to_dict(orient='records'),
            'explained_variance': explained_variance.tolist(),
            'features': df.columns.tolist()
        })

    # Weibull分布
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
            scale_param = reliability.mtbf * 24 if reliability.mtbf is not None else 24

            if scale_param <= 0:
                continue

            shape_params = [0.5, 1.0, 3.0]
            x = np.linspace(0, 3000, 1000)
            pdf_initial = weibull_min.pdf(x, shape_params[0], scale=scale_param)
            pdf_random = weibull_min.pdf(x, shape_params[1], scale=scale_param)
            pdf_wearout = weibull_min.pdf(x, shape_params[2], scale=scale_param)

            pdf_initial = np.nan_to_num(pdf_initial, nan=0.0, posinf=0.0, neginf=0.0)
            pdf_random = np.nan_to_num(pdf_random, nan=0.0, posinf=0.0, neginf=0.0)
            pdf_wearout = np.nan_to_num(pdf_wearout, nan=0.0, posinf=0.0, neginf=0.0)

            bathtub_curve = pdf_initial + pdf_random + pdf_wearout

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
                'slope': slope,
                'isWearoutIncreasing': is_wearout_increasing
            })

        if not data:
            return Response({'error': 'No valid MTBF data found'}, status=400)

        return Response(data)



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






