from rest_framework import serializers
from accounts.models import CustomUser
from .models import NearMiss, CompanyCode,SafetyIndicators,TrendSafetyIndicators

from rest_framework import serializers



# serializers.py
from rest_framework import serializers
from .models import NearMiss, CompanyCode, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('userName', 'email')

class NearMissSerializer(serializers.ModelSerializer):
    companyCode = serializers.CharField()  # companyCodeを文字列として扱う
    userName = UserSerializer()  # userNameをUserSerializerとして扱う

    class Meta:
        model = NearMiss
        fields = [
            'id', 'companyCode', 'nearMissNo', 'userName', 'department',
            'dateOfOccurrence', 'placeOfOccurrence', 'typeOfAccident', 'description',
            'factor', 'injuredLv', 'equipmentDamageLv', 'affectOfEnviroment', 'newsCoverage',
            'measures', 'actionItems', 'solvedActionItems', 'createdDay'
        ]

    # createメソッドを明示的に実装する
    def create(self, validated_data):
        company_code_data = validated_data.pop('companyCode', None)
        if company_code_data:
            company_code = CompanyCode.objects.filter(companyCode=company_code_data).first()
            if not company_code:
                company_code = CompanyCode.objects.create(companyCode=company_code_data)
        else:
            company_code = None

        user_data = validated_data.pop('userName')
        user_name = user_data.get('userName')
        email = user_data.get('email', None)

        user, created = CustomUser.objects.get_or_create(userName=user_name)
        if created:
            user.email = email
            user.save()
        elif email and user.email != email:
            user.email = email
            user.save()

        near_miss = NearMiss.objects.create(
            companyCode=company_code,
            userName=user,
            **validated_data
        )
        return near_miss

    # updateメソッドを追加してネストされたフィールドも更新できるようにする
    def update(self, instance, validated_data):
        # companyCode の更新処理
        company_code_data = validated_data.pop('companyCode', None)
        if company_code_data:
            company_code = CompanyCode.objects.filter(companyCode=company_code_data).first()
            if not company_code:
                company_code = CompanyCode.objects.create(companyCode=company_code_data)
            instance.companyCode = company_code

        # userName の更新処理
        user_data = validated_data.pop('userName', None)
        if user_data:
            user_name = user_data.get('userName')
            email = user_data.get('email', None)

            user, created = CustomUser.objects.get_or_create(userName=user_name)
            if created:
                user.email = email
                user.save()
            elif email and user.email != email:
                user.email = email
                user.save()

            instance.userName = user  # userオブジェクトを更新

        # その他のフィールドの更新処理
        instance.department = validated_data.get('department', instance.department)
        instance.dateOfOccurrence = validated_data.get('dateOfOccurrence', instance.dateOfOccurrence)
        instance.placeOfOccurrence = validated_data.get('placeOfOccurrence', instance.placeOfOccurrence)
        instance.typeOfAccident = validated_data.get('typeOfAccident', instance.typeOfAccident)
        instance.description = validated_data.get('description', instance.description)
        instance.factor = validated_data.get('factor', instance.factor)
        instance.injuredLv = validated_data.get('injuredLv', instance.injuredLv)
        instance.equipmentDamageLv = validated_data.get('equipmentDamageLv', instance.equipmentDamageLv)
        instance.affectOfEnviroment = validated_data.get('affectOfEnviroment', instance.affectOfEnviroment)
        instance.newsCoverage = validated_data.get('newsCoverage', instance.newsCoverage)
        instance.measures = validated_data.get('measures', instance.measures)
        instance.actionItems = validated_data.get('actionItems', instance.actionItems)
        instance.solvedActionItems = validated_data.get('solvedActionItems', instance.solvedActionItems)

        # インスタンスを保存して更新
        instance.save()

        return instance



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
