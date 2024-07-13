from rest_framework import serializers
from accounts.models import CompanyCode
from ceList.models import Equipment,Machine 
from .models import FailureData, WeibullData, TroubleHistory





#TroubleHistoryモデルのシリアライザー
#------------------------------------------------------------------------------------------------------

class TroubleHistorySerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )

    class Meta:
        model = TroubleHistory #呼び出すモデル名
        fields = ['companyCode','equipment','machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'rootCause',] #表示したいフィールド名


class CompanyTroubleHistorySerializer(serializers.ModelSerializer):
    troubleHistory = TroubleHistorySerializer(many=True, source='troubleHistory_companyCode')#ここのsourceは本当に注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'troubleHistory']


#------------------------------------------------------------------------------------------------------








# 故障データモデルのシリアライザー
class FailureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailureData
        fields = '__all__'  # 全フィールドをシリアライズ



#ワイブルデータのシリアライザー
class WeibullDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeibullData
        fields = ['failure_time']



from .models import BayesianPrediction

class BayesianPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BayesianPrediction
        fields = '__all__'  # 全フィールドをシリアライズ