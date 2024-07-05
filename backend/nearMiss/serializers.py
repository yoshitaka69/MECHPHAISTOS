from rest_framework import serializers
from accounts.models import CustomUser
from .models import NearMiss, CompanyCode,SafetyIndicators,TrendSafetyIndicators

from rest_framework import serializers



from rest_framework import serializers
from .models import NearMiss, CompanyCode, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('userName',)  # ここでユーザー名のみをシリアライズ

class NearMissSerializer(serializers.ModelSerializer):
    userName = UserSerializer()
    companyCode = serializers.SlugRelatedField(slug_field='companyCode', queryset=CompanyCode.objects.all())
    dateOfOccurrence = serializers.DateField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = NearMiss
        fields = [
            'companyCode', 'nearMissNo', 'userName', 'department', 'dateOfOccurrence', 'placeOfOccurrence', 
            'typeOfAccident', 'factor', 'injuredLv', 'equipmentDamageLv', 'affectOfEnviroment', 
            'newsCoverage', 'measures', 'actionItems', 'solvedActionItems', 'description', 'updateDay'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('userName')
        user, created = CustomUser.objects.get_or_create(userName=user_data['userName'])
        company_code = validated_data.pop('companyCode')
        near_miss = NearMiss.objects.create(userName=user, companyCode=company_code, **validated_data)
        return near_miss






class CompanyNearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissSerializer(many=True, read_only=True, source='nearMiss_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'nearMissList']








#SafetyIndicator
class SafetyIndicatorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SafetyIndicators
        fields = ['companyCode', 'companyName', 'safetyIndicators', 'dangerArea','totalOfNearMiss', 'countOfLevelA', 'rateOflevelA', 'countOfActionItems', 'countOfSolvedActionItems', 'rateOfActionItems']

class CompanySafetyIndicatorsSerializer(serializers.ModelSerializer):
    safetyIndicatorsList = SafetyIndicatorsSerializer(many=True, read_only=True, source='safetyIndicators_companyCode')
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'safetyIndicatorsList']






#SafetyIndicator Trend
class TrendSafetyIndicatorsSerializer(serializers.ModelSerializer):
        
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode',  # companyCode モデルの表示したい文字列フィールド
        queryset=CompanyCode.objects.all()
    )

    safetyIndicators = serializers.SlugRelatedField(
        slug_field='safetyIndicators', 
        queryset=SafetyIndicators.objects.all()
    )

    class Meta:
        model = TrendSafetyIndicators
        fields = ['companyCode', 'companyName', 'safetyIndicators', 'lastUpdateDay',]


class CompanyTrendSafetyIndicatorsSerializer(serializers.ModelSerializer):
    trendSafetyIndicatorsList = TrendSafetyIndicatorsSerializer(many=True, read_only=True, source='trendSafetyIndicators_companyCode')
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'trendSafetyIndicatorsList']
