from rest_framework import serializers
from accounts.models import CustomUser
from .models import NearMiss, CompanyCode,SafetyIndicators

from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('userName',)  # ここでユーザー名のみをシリアライズ

class NearMissSerializer(serializers.ModelSerializer):
    userName = UserSerializer() 
    dateOfOccurrence = serializers.DateField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)

    class Meta:
        model = NearMiss
        fields = ['nearMissNo','userName','department','dateOfOccurrence','placeOfOccurrence','typeOfAccident','factor','injuredLv','equipmentDamageLv','affectOfEnviroment','newsCoverage','measures','description','updateDay',]


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

