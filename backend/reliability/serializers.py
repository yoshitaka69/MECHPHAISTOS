from rest_framework import serializers
from accounts.models import CompanyCode
from ceList.models import Equipment,Machine 
from .models import TroubleHistory,FailurePredictionPoint,Reliability



# Reliabilityモデル
#------------------------------------------------------------------------------------------------------

from rest_framework import serializers
from .models import Reliability, CompanyCode

class ReliabilitySerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',
        queryset=CompanyCode.objects.all()
    )

    class Meta:
        model = Reliability
        fields = [
            'companyCode', 'ceListNo', 'plant', 'equipment', 'machineName', 
            'failureType',  'operationalCondition', 
            'PMType', 'maintenanceMethod', 'maintenanceFrequency', 
            'failureMode', 'failureCause', 
            'componentCondition', 'mttr', 'mtbf', 'mttf', 
            'totalOperatingTime', 'failureCount', 'failureDate', 'record_date'
        ]

        

class CompanyReliabilitySerializer(serializers.ModelSerializer):
    # related_name='reliability_companyCode'を正しく使用
    reliability = ReliabilitySerializer(many=True, source='reliability_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'reliability']


#------------------------------------------------------------------------------------------------------






# 故障履歴モデル(PrecisionAndAccuracy)
#------------------------------------------------------------------------------------------------------

class TroubleHistorySerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',
        queryset=CompanyCode.objects.all()
    )

    class Meta:
        model = TroubleHistory
        fields = ['companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause']

class CompanyTroubleHistorySerializer(serializers.ModelSerializer):
    troubleHistory = TroubleHistorySerializer(many=True, source='troubleHistory_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'troubleHistory']

#------------------------------------------------------------------------------------------------------





# 故障予測ポイントモデル(PrecisionAndAccuracy)
#------------------------------------------------------------------------------------------------------

class FPPSerializer(serializers.ModelSerializer):
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',
        queryset=CompanyCode.objects.all()
    )

    class Meta:
        model = FailurePredictionPoint
        fields = ['companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType']

class CompanyFPPSerializer(serializers.ModelSerializer):
    failurePredictionPoint = FPPSerializer(many=True, source='failurePredictionPoint_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'failurePredictionPoint']

#------------------------------------------------------------------------------------------------------



