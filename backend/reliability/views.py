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



    #信頼性のパラメータを取得
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






    @action(detail=False, methods=['get'], url_path='bayesian_prediction')
    def bayesian_prediction(self, request):
        """
        Perform Bayesian prediction using reliability data to estimate future failures.
        信頼性データを使用して将来の故障を推定するベイジアン予測を行います。
        """

        # クエリパラメータから会社コードを取得
        company_code = request.query_params.get('companyCode', None)
        # スライディングウィンドウのサイズ（日数）を取得。デフォルトは365日
        window_size = int(request.query_params.get('windowSize', 365))  
        # スライディングウィンドウのステップサイズ（日数）を取得。デフォルトは30日
        step_size = int(request.query_params.get('stepSize', 30))  

        # 会社コードが提供されていない場合はエラーレスポンスを返す
        if not company_code:
            return Response({'error': 'companyCode is required'}, status=400)

        # 会社コードに関連する信頼性エントリをデータベースから取得
        reliability_entries = Reliability.objects.filter(companyCode__companyCode=company_code)

        # 該当する信頼性エントリがない場合、エラーレスポンスを返す
        if not reliability_entries.exists():
            return Response({'error': 'No reliability entries found for this companyCode'}, status=404)

        # 予測結果を格納するリスト
        predictions = []
        # 今日の日付を取得
        today = datetime.date.today()

        # 各信頼性エントリに対して予測を行うループ
        for reliability in reliability_entries:
            # 必要なパラメータがNoneの場合はデフォルト値を設定
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

            # スライディングウィンドウの開始日と終了日を設定
            start_date = today - datetime.timedelta(days=window_size)
            end_date = start_date + datetime.timedelta(days=window_size)

            # 終了日が今日の日付より前になるまで予測を繰り返す
            while end_date <= today:
                # 事前分布の平均を設定（故障タイプの影響を考慮）
                prior_mean = mtbf * (1 - 0.1 * failure_type)

                # 事前分布の標準偏差を設定（保全の影響を考慮）
                prior_std = mttr / 2 * (1 + 0.1 * maintenance_impact)

                # 尤度の平均を設定（保全頻度の影響を考慮）
                likelihood_mean = mttf * (1 + 0.05 * maintenance_frequency)

                # 尤度の標準偏差を設定
                likelihood_std = mttr / 2

                # 事後分布の平均を計算
                posterior_mean = (prior_mean + likelihood_mean) / 2

                # 事後分布の標準偏差を計算
                posterior_std = (prior_std + likelihood_std) / 2

                # 故障予測のためのx軸の範囲を設定
                x = np.linspace(0, 1000, 100)

                # 事後分布の確率密度関数を計算
                posterior_pdf = norm.pdf(x, posterior_mean, posterior_std)

                # 予測データを辞書形式でリストに追加
                predictions.append({
                    'companyCode': reliability.companyCode.companyCode,  # 会社コード
                    'ceListNo': reliability.ceListNo.id if reliability.ceListNo else None,  # CEリスト番号
                    'mttr': mttr,  # MTTR（平均修理時間）
                    'mtbf': mtbf,  # MTBF（平均故障間隔）
                    'mttf': mttf,  # MTTF（平均故障時間）
                    'totalOperatingTime': reliability.totalOperatingTime,  # 総稼働時間
                    'failureCount': reliability.failureCount,  # 故障回数
                    'failureType': failure_type,  # 故障タイプ
                    'failureTypeImpact': failure_type * 10,  # 故障タイプの影響度
                    'failureMode': failure_mode,  # 故障モード
                    'maintenanceMethod': maintenance_method,  # 保全方法
                    'maintenanceMethodImpact': maintenance_method * 5,  # 保全方法の影響度
                    'maintenanceFrequency': maintenance_frequency,  # 保全頻度
                    'maintenanceImpact': maintenance_impact,  # 保全の影響
                    'failureCause': failure_cause,  # 故障原因
                    'failureCauseImpact': failure_cause * 7,  # 故障原因の影響度
                    'operationalCondition': operational_condition,  # 運転状態
                    'operationalConditionImpact': operational_condition * 2,  # 運転状態の影響度
                    'componentCondition': component_condition,  # 部品状態
                    'componentConditionImpact': component_condition * 4,  # 部品状態の影響度
                    'PMType': pm_type,  # PMタイプ
                    'PMTypeImpact': 1,  # PMタイプの影響度は1
                    'x': x.tolist(),  # x軸の値
                    'posterior_pdf': posterior_pdf.tolist(),  # 事後分布の確率密度関数
                    'start_date': start_date,  # ウィンドウ開始日
                    'end_date': end_date,  # ウィンドウ終了日
                })

                # ウィンドウの開始日と終了日をステップサイズ分だけ進める
                start_date += datetime.timedelta(days=step_size)
                end_date += datetime.timedelta(days=step_size)

        # 予測結果をレスポンスとして返す
        return Response(predictions)






    #相関行列のヒートマップ
    @action(detail=False, methods=['get'], url_path='correlation')
    def get_heatmap_data(self, request):
        """
        Calculate the correlation matrix of various reliability factors and return the data for heatmap visualization.
        信頼性要因の相関行列を計算し、ヒートマップのデータを返します。
        """
        print("Debug: get_heatmap_data called")
        
        # クエリパラメータから会社コードを取得
        company_code = request.query_params.get('companyCode')

        # 会社コードが提供されていない場合、エラーメッセージを返す
        if not company_code:
            print("Error: companyCode parameter is missing")
            return Response({"error": "companyCode parameter is required"}, status=400)

        # 会社コードに関連する信頼性データを取得
        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        # 信頼性データが存在しない場合、エラーメッセージを返す
        if not reliabilities.exists():
            print(f"Error: No data found for companyCode {company_code}")
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # 信頼性データを格納するリスト
            data = []
            for reliability in reliabilities:
                # 各信頼性データの項目を抽出し、データフレームの作成に使用
                data.append({
                    "MTTR": reliability.mttr,  # MTTR（平均修理時間）
                    "MTBF": reliability.mtbf,  # MTBF（平均故障間隔）
                    "MTTF": reliability.mttf,  # MTTF（平均故障時間）
                    "failureCount": reliability.failureCount,  # 故障回数
                    "totalOperatingTime": reliability.totalOperatingTime,  # 総稼働時間
                    "failureType": reliability.failureType,  # 故障タイプ
                    "failureMode": reliability.failureMode,  # 故障モード
                    "maintenanceMethod": reliability.maintenanceMethod,  # 保全方法
                    "maintenanceFrequency": reliability.maintenanceFrequency,  # 保全頻度（追加）
                    "PMType": reliability.PMType,  # PMタイプ（予防保全など）
                    "failureCause": reliability.failureCause,  # 故障原因
                    "operationalCondition": reliability.operationalCondition,  # 運転状態
                    "componentCondition": reliability.componentCondition  # 部品状態
                })

            # データフレームの作成
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

            # ヒートマップデータの形式に変換
            heatmap_data = correlation_matrix.reset_index().melt(id_vars=['index'])
            heatmap_data.columns = ['x', 'y', 'value']  # ヒートマップ形式に整形

            # 整形されたヒートマップデータをレスポンスとして返す
            return Response(heatmap_data.to_dict(orient='records'))

        except Exception as e:
            # エラーが発生した場合はログを出力し、エラーレスポンスを返す
            print(f"Error: {str(e)}")
            return Response({"error": "An error occurred while processing the request."}, status=500)

        







    #ランダムフォレストによる特徴量の重要度
    @action(detail=False, methods=['get'], url_path='feature_importance_details')
    def get_feature_importance_details(self, request):

        """
        Extract feature importance details for reliability data.
        信頼性データの特徴量重要度を抽出します。
        """

        company_code = request.query_params.get('companyCode')

        # companyCodeが提供されていない場合、エラーメッセージを返す
        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        # 会社コードに関連する信頼性データを取得
        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        # 信頼性データが存在しない場合、エラーメッセージを返す
        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # 信頼性データをDataFrame形式で整理
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  # MTTR（平均修理時間）
                    "MTBF": reliability.mtbf,  # MTBF（平均故障間隔）
                    "MTTF": reliability.mttf,  # MTTF（平均故障時間）
                    "failureCount": reliability.failureCount,  # 故障回数
                    "totalOperatingTime": reliability.totalOperatingTime,  # 総稼働時間
                    "failureType": reliability.failureType,  # 故障タイプ
                    "failureMode": reliability.failureMode,  # 故障モード
                    "maintenanceMethod": reliability.maintenanceMethod,  # 保全方法
                    "maintenanceFrequency": reliability.maintenanceFrequency,  # 保全頻度
                    "PMType": reliability.PMType,  # PMタイプ（予防保全など）
                    "failureCause": reliability.failureCause,  # 故障原因
                    "operationalCondition": reliability.operationalCondition,  # 運転状態
                    "componentCondition": reliability.componentCondition  # 部品状態
                })

            # データフレームに変換
            df = pd.DataFrame(data)

            # 特徴量（X）と目的変数（y）に分割
            X = df.drop(columns=['failureCount'])  # `failureCount` を目的変数とする
            y = df['failureCount']

            # ランダムフォレストモデルの訓練
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X, y)

            # 特徴量重要度を取得
            importance = model.feature_importances_
            features = X.columns

            # 特徴量と重要度を表示
            feature_importance = [{"feature": f, "importance": round(imp, 2)} for f, imp in zip(features, importance)]

            # トレーニングデータの一部と予測結果を抽出
            training_data = X.head(10).to_dict(orient='records')  # トレーニングデータの例
            predictions = model.predict(X.head(10)).tolist()  # 予測結果の例

            # 結果をJSON形式にフォーマット
            response_data = {
                "training_data": training_data,
                "predictions": predictions,
                "feature_importance": feature_importance
            }

            return Response(response_data)

        except Exception as e:
            # エラー発生時の例外処理
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)


        



    
    #特徴料重要度と回帰分析
    @action(detail=False, methods=['get'], url_path='regression_analysis')
    def get_regression_analysis(self, request):
        """
        Conduct regression analysis based on reliability data using MTTF.
        信頼性データを基にMTTFを使用して回帰分析を実行します。
        """
        company_code = request.query_params.get('companyCode')

        # companyCodeが提供されていない場合のエラーレスポンス
        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        # 会社コードに基づいて信頼性データを取得
        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        # 該当データが存在しない場合のエラーレスポンス
        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # 信頼性データを格納するリスト
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  # MTTR（平均修理時間）
                    "MTBF": reliability.mtbf,  # MTBF（平均故障間隔）
                    "MTTF": reliability.mttf,  # MTTF（平均故障時間）
                    "failureCount": reliability.failureCount,  # 故障回数
                    "totalOperatingTime": reliability.totalOperatingTime,  # 総稼働時間
                    "failureType": reliability.failureType,  # 故障タイプ
                    "failureMode": reliability.failureMode,  # 故障モード
                    "maintenanceMethod": reliability.maintenanceMethod,  # 保全方法
                    "maintenanceFrequency": reliability.maintenanceFrequency,  # 保全頻度
                    "failureCause": reliability.failureCause,  # 故障原因
                    "operationalCondition": reliability.operationalCondition,  # 運転状態
                    "componentCondition": reliability.componentCondition,  # 部品状態
                    "PMType": reliability.PMType  # PMタイプ（追加）
                })

            df = pd.DataFrame(data)

            # 回帰分析のターゲットを MTTF に変更
            features = df.columns.drop('MTTF')
            regression_results = {}

            for feature in features:
                X = df[[feature]].fillna(0)
                y = df['MTTF'].fillna(0)  # MTTFをターゲットに設定

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


        





    #SHAP値の取得
    @action(detail=False, methods=['get'], url_path='shap_values') 
    def get_shap_values(self, request):
        """
        Calculate SHAP values for the reliability data to explain model predictions.
        信頼性データに基づき、モデル予測を説明するためのSHAP値を計算します。
        """
        # クエリパラメータから会社コードを取得
        company_code = request.query_params.get('companyCode')

        # 会社コードが提供されていない場合、エラーメッセージを返す
        if not company_code:
            return Response({"error": "companyCode parameter is required"}, status=400)

        # 会社コードに関連する信頼性データを取得
        reliabilities = Reliability.objects.filter(companyCode__companyCode=company_code)

        # 信頼性データが存在しない場合、エラーメッセージを返す
        if not reliabilities.exists():
            return Response({"error": "No data found for the given companyCode"}, status=404)

        try:
            # 信頼性データを格納するリストを作成
            data = []
            for reliability in reliabilities:
                data.append({
                    "MTTR": reliability.mttr,  # MTTR（平均修理時間）
                    "MTBF": reliability.mtbf,  # MTBF（平均故障間隔）
                    "MTTF": reliability.mttf,  # MTTF（平均故障時間）
                    "failureCount": reliability.failureCount,  # 故障回数
                    "totalOperatingTime": reliability.totalOperatingTime,  # 総稼働時間
                    "failureType": reliability.failureType,  # 故障タイプ
                    "failureMode": reliability.failureMode,  # 故障モード
                    "maintenanceMethod": reliability.maintenanceMethod,  # 保全方法
                    "maintenanceFrequency": reliability.maintenanceFrequency,  # 保全頻度
                    "failureCause": reliability.failureCause,  # 故障原因
                    "operationalCondition": reliability.operationalCondition,  # 運転状態
                    "componentCondition": reliability.componentCondition,  # 部品状態
                    "PMType": reliability.PMType  # PMタイプ（予防保全など）追加
                })

            # データフレームに変換
            df = pd.DataFrame(data)
            features = df.columns  # 特徴量を取得
            X = df.fillna(0)  # NaN値を0に置き換え

            # ランダムフォレストモデルのトレーニング
            model = RandomForestRegressor()
            model.fit(X, X["failureCount"])  # 例として故障回数をターゲット変数として使用

            # SHAP値を計算（モデルの予測を説明するための値）
            explainer = shap.TreeExplainer(model)  # SHAPの説明モデルを設定
            shap_values = explainer.shap_values(X)  # SHAP値を計算

            # SHAP値を整形し、各特徴量に対応させたデータを作成
            shap_data = []
            for i in range(len(shap_values)):
                shap_data.append({feature: shap_values[i][j] for j, feature in enumerate(features)})

            # SHAP値と特徴量のリストをレスポンスとして返す
            return Response({"shap_values": shap_data, "features": features.tolist()})

        except Exception as e:
            # エラー発生時の例外処理
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)

        




    #PCAの実行
    @action(detail=False, methods=['get'], url_path='pca')
    def perform_pca(self, request):
        """
        Perform PCA (Principal Component Analysis) on reliability data for dimensionality reduction.
        信頼性データに対して主成分分析（PCA）を実行し、次元削減を行います。
        """
        # クエリパラメータから会社コードを取得
        company_code = request.query_params.get('companyCode')
        
        # 会社コードに基づいてCompanyCodeモデルから会社情報を取得
        company = CompanyCode.objects.filter(companyCode=company_code).first()
        
        # 会社コードが存在しない場合のエラーレスポンス
        if not company:
            return Response({"error": "Company code not found."}, status=404)

        # 会社コードに基づいてReliabilityモデルから信頼性データを取得
        queryset = Reliability.objects.filter(companyCode=company)

        # 必要な信頼性データの項目を抽出
        data = queryset.values(
            'mttr', 'mtbf', 'mttf', 'failureCount', 'totalOperatingTime', 
            'failureType', 'failureMode', 'maintenanceMethod', 'maintenanceFrequency', 
            'failureCause', 'operationalCondition', 'componentCondition', 'PMType'  # PMTypeを追加、maintenanceImpactを削除
        )

        # データフレームを作成（リスト化してPandasのDataFrameに変換）
        df = pd.DataFrame(list(data))

        # PCA（主成分分析）の実行。主成分を2つに減らす設定
        pca = PCA(n_components=2)  # 主成分を2つに制限
        pca_result = pca.fit_transform(df.fillna(0))  # null値を0に変換しPCAを適用

        # 主成分得点を取得し、PC1とPC2のカラム名を付ける
        pca_scores = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])

        # 各主成分の寄与率（データ全体の分散をどの程度説明しているか）を取得
        explained_variance = pca.explained_variance_ratio_

        # 主成分得点、寄与率、および特徴量名をレスポンスとして返す
        return Response({
            'pca_scores': pca_scores.to_dict(orient='records'),  # 主成分得点をJSON形式に変換して返す
            'explained_variance': explained_variance.tolist(),  # 各主成分の寄与率をリスト形式で返す
            'features': df.columns.tolist()  # データの特徴量（項目名）をリスト形式で返す
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






