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
        return NearMiss.objects.filter(companyCode=obj.companyCode).count()

    def get_rate_of_level_a(self, obj):
        total_near_miss = NearMiss.objects.filter(companyCode=obj.companyCode).count()
        if total_near_miss > 0:
            level_a_count = NearMiss.objects.filter(companyCode=obj.companyCode, measures__contains='A').count()
            return (level_a_count / total_near_miss) * 100
        else:
            return 0

    def get_rate_of_action_items(self, obj):
        total_action_items = obj.ActionItems.count()
        solved_action_items = obj.solvedActionItems.count()
        if total_action_items > 0:
            return (solved_action_items / total_action_items) * 100
        else:
            return 0

    def get_safety_indicators(self, obj):
        rate_of_level_a = self.get_rate_of_level_a(obj)
        rate_of_action_items = self.get_rate_of_action_items(obj)
        if rate_of_level_a >= 40:
            return 'High'
        elif rate_of_level_a < 40:
            if rate_of_action_items > 80:
                return 'High'
            elif 40 < rate_of_action_items <= 80:
                return 'Middle'
            elif 0 < rate_of_action_items <= 40:
                return 'Low'
        return 'Undefined'
