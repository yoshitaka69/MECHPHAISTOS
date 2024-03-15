from rest_framework import serializers
from .models import NearMiss, CompanyCode, ActionItemList, SafetyIndicators
from django.db.models import Count, Q

class NearMissSerializer(serializers.ModelSerializer):
    nearMissNo = serializers.CharField(read_only=True)
    dateOfOccurrence = serializers.DateField(format="%Y-%m-%d")
    createdDay = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    updateDay = serializers.DateTimeField(format="%Y-%m-%d",read_only=True)
    safetyIndicater = serializers.CharField(read_only=True)

    class Meta:
        model = NearMiss
        fields = ['id','companyCode','companyName','nearMissNo','userName','department','dateOfOccurrence','placeOfOccurrence','typeOfAccident','factor','injuredLv','equipmentDamageLv','affectOfEnviroment','newsCoverage','measures','safetyIndicater','description','createdDay','updateDay',]
        #fields = '__all__'

    userに対するForeignKeyのfillter機能
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            # 特定の masterCode を持つユーザーの場合、すべてのレコードを表示
            if user.companyCode.masterCode == 'MASTER123':
                return MyModel.objects.all()
            # それ以外のユーザーにはその companyCode に関連するレコードのみを表示
            else:
                return MyModel.objects.filter(companyCode=user.companyCode)
        else:
            # 認証されていないユーザーには空のクエリセットを返す
            return MyModel.objects.none()
    
    def create(self, validated_data):
    # companyName から値を取得
    company_name = validated_data.get('companyName', '')
    if company_name:
        # companyName に基づいて連番を生成
        last_near_miss = NearMiss.objects.filter(nearMissNo__startswith=company_name).order_by('-nearMissNo').first()

        if last_near_miss:
            # companyName で切り出した後の数字の部分を取得
            try:
                last_number_str = last_near_miss.nearMissNo.split(company_name + '-')[1]
                last_number = int(last_number_str)
                new_code_number = last_number + 1
            except (IndexError, ValueError):
                new_code_number = 1
        else:
            new_code_number = 1

        validated_data['nearMissNo'] = f'{company_name}-{str(new_code_number).zfill(3)}'
    else:
        # companyName が提供されていない場合、デフォルトの連番を使用
        validated_data['nearMissNo'] = 'default-001'

    return NearMiss.objects.create(**validated_data)


class CompanyNearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissSerializer(many=True, read_only=True, source='nearMiss_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'nearMissList']



class ActionitemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActionItemList
        fields = fields = ['companyCode', 'companyName', 'actionItems', 'solvedActionItems']

    

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
