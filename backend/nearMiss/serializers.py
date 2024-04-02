from rest_framework import serializers
from accounts.models import CustomUser
from .models import NearMiss, CompanyCode, ActionItemList, SafetyIndicators

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












#ActionItemList
class ActionItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActionItemList
        fields = fields = ['companyCode', 'companyName', 'actionItems', 'solvedActionItems']






#SafetyIndicator
class SafetyIndicatorsSerializer(serializers.ModelSerializer):
    safetyIndicators = serializers.SerializerMethodField()
    totalOfNearMiss = serializers.SerializerMethodField()
    rateOflevelA = serializers.SerializerMethodField()
    rateOfActionItems = serializers.SerializerMethodField()
    
    class Meta:
        model = SafetyIndicators
        fields = ['companyCode', 'companyName', 'safetyIndicators', 'totalOfNearMiss', 'rateOflevelA', 'ActionItems', 'solvedActionItems', 'rateOfActionItems']


    def get_total_of_near_miss(self, obj):
        return obj.total_of_near_miss()

    def get_rate_of_level_a(self, obj):
        return obj.rate_of_level_a()

    def get_rate_of_action_items(self, obj):
        return obj.rate_of_action_items()

    def get_safety_indicators(self, obj):
        return obj.calculate_safety_indicators()
