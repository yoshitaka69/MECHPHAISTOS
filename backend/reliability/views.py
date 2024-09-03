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
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA  # ここでPCAをインポート
from sklearn.linear_model import LinearRegression
import shap


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




    #相関行列のヒートマップ
    @action(detail=False, methods=['get'], url_path='correlation')
    def get_heatmap_data(self, request):
        print("Debug: get_heatmap_data called")
        company_code = request.query_params.get('companyCode')

        if not company_code:
            print("Error: companyCode parameter is missing")
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            print(f"Error: No data found for companyCode {company_code}")
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # データフレームを作成
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
                    "maintenanceImpact": reliability.maintenanceImpact,
                    "failureCause": reliability.failureCause,
                    "environmentCondition": reliability.environmentCondition,
                    "operationalCondition": reliability.operationalCondition,
                    "componentCondition": reliability.componentCondition,
                })

            df = pd.DataFrame(data)
            print("Debug: DataFrame created")
            print(df)

            # 相関行列を計算
            correlation_matrix = df.corr()
            print("Debug: Correlation matrix calculated")
            print(correlation_matrix)

            # NaNやInfinityを0に置き換え
            correlation_matrix = correlation_matrix.replace([np.inf, -np.inf], np.nan).fillna(0)

            # 小数点以下2桁までにフォーマット
            correlation_matrix = correlation_matrix.round(2)
            print("Debug: Correlation matrix after rounding")
            print(correlation_matrix)

            # JSON形式で返すために整形
            heatmap_data = correlation_matrix.reset_index().melt(id_vars=['index'])
            heatmap_data.columns = ['x', 'y', 'value']

            return Response(heatmap_data.to_dict(orient='records'))

        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({"error": "An error occurred while processing the request."}, status=500)
        





    #ランダムフォレストによる特徴量の重要度
    @action(detail=False, methods=['get'], url_path='feature_importance_details')
    def get_feature_importance_details(self, request):
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # データフレームを作成
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
                    "maintenanceImpact": reliability.maintenanceImpact,
                    "failureCause": reliability.failureCause,
                    "environmentCondition": reliability.environmentCondition,
                    "operationalCondition": reliability.operationalCondition,
                    "componentCondition": reliability.componentCondition,
                })

            df = pd.DataFrame(data)

            # 特徴量と目的変数の分割
            X = df.drop(columns=['failureCount'])  # 例として `failureCount` を目的変数とする
            y = df['failureCount']

            # ランダムフォレストモデルの訓練
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X, y)

            # 特徴量重要度の抽出
            importance = model.feature_importances_
            features = X.columns

            # トレーニングデータと評価結果の例を取得
            training_data = X.head(10).to_dict(orient='records')  # トレーニングデータの一部を返す
            predictions = model.predict(X.head(10)).tolist()  # 一部の予測結果を返す

            # 結果をJSON形式に整形して返す
            feature_importance = [{"feature": f, "importance": round(imp, 2)} for f, imp in zip(features, importance)]
            response_data = {
                "training_data": training_data,
                "predictions": predictions,
                "feature_importance": feature_importance
            }

            return Response(response_data)

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)
        

    
    #特徴料重要度と回帰分析
    @action(detail=False, methods=['get'], url_path='regression_analysis')
    def get_regression_analysis(self, request):
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # データフレームを作成
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
                    "maintenanceImpact": reliability.maintenanceImpact,
                    "failureCause": reliability.failureCause,
                    "environmentCondition": reliability.environmentCondition,
                    "operationalCondition": reliability.operationalCondition,
                    "componentCondition": reliability.componentCondition,
                    "failureTime": reliability.failureCount  # 例として故障回数を故障時間に使用
                })

            df = pd.DataFrame(data)

            features = df.columns.drop('failureTime')
            regression_results = {}

            for feature in features:
                X = df[[feature]].fillna(0)
                y = df['failureTime'].fillna(0)

                model = LinearRegression()
                model.fit(X, y)

                slope = model.coef_[0]
                intercept = model.intercept_

                # 信頼区間の計算
                y_pred = model.predict(X)
                n = len(X)
                mean_x = np.mean(X[feature])
                t_value = 1.96  # 95%の信頼区間
                se = np.sqrt(np.sum((y - y_pred) ** 2) / (n - 2))
                se_line = se * np.sqrt(1 / n + (X[feature] - mean_x) ** 2 / np.sum((X[feature] - mean_x) ** 2))

                lower_bound = y_pred - t_value * se_line
                upper_bound = y_pred + t_value * se_line

                # NaNや無限大の値をゼロに置き換える
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
        




    
    @action(detail=False, methods=['get'], url_path='shap_values')
    def get_shap_values(self, request):
        company_code = request.query_params.get('companyCode')

        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # データフレームを作成
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
                    "maintenanceImpact": reliability.maintenanceImpact,
                    "failureCause": reliability.failureCause,
                    "environmentCondition": reliability.environmentCondition,
                    "operationalCondition": reliability.operationalCondition,
                    "componentCondition": reliability.componentCondition,
                })

            df = pd.DataFrame(data)
            features = df.columns
            X = df.fillna(0)

            # ランダムフォレストモデルをトレーニング
            model = RandomForestRegressor()
            model.fit(X, X["failureCount"])  # 例として故障回数をターゲットとする

            # SHAP値の計算
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X)

            shap_data = []
            for i in range(len(shap_values)):
                shap_data.append({feature: shap_values[i][j] for j, feature in enumerate(features)})

            return Response({"shap_values": shap_data, "features": features.tolist()})

        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)
        


    #PCAの実行
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
            'maintenanceImpact', 'failureCause', 'environmentCondition', 
            'operationalCondition', 'componentCondition'
        )

        # データフレームを作成
        df = pd.DataFrame(list(data))

        # PCAの実行
        pca = PCA(n_components=2)  # 2つの主成分を取得
        pca_result = pca.fit_transform(df.fillna(0))  # null値を0に変換

        # 主成分得点を取得
        pca_scores = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])

        # 寄与率を取得
        explained_variance = pca.explained_variance_ratio_

        return Response({
            'pca_scores': pca_scores.to_dict(orient='records'),
            'explained_variance': explained_variance.tolist(),
            'features': df.columns.tolist()
        })


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






