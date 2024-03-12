from rest_framework import serializers
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05


class PlannedPM02Serializer(serializers.ModelSerializer):
    plannedMonth = serializers.DateTimeField(format="%Y-%m-%d")
    totalCost = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = PlannedPM02 # 呼び出すモデル
        fields = '__all__' # API上に表示するモデルのデータ項目
        
    def get_totalCost(self, obj):
        return sum(getattr(obj, month, 0) or 0 for month in ['jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    def update(self, instance, validated_data):
        # 各月のデータを更新
        for month in ['jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            if month in validated_data:
                setattr(instance, month, validated_data[month])

        # インスタンスを保存
        instance.save()

        # totalCostを更新
        instance.totalCost = self.get_totalCost(instance)
        instance.save()

        return instance



class CompanyCodePPM02Serializer(serializers.ModelSerializer):
    plannedPM02List = PlannedPM02Serializer(many=True, read_only=True, source='plannedPM02_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM02List']



#Actual PM02 cost
class ActualPM02Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM02
        fields = '__all__'

class CompanyCodeAPM02Serializer(serializers.ModelSerializer):
    actualPM02List = ActualPM02Serializer(many=True, read_only=True, source='actualPM02_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM02List']




class PlannedPM03Serializer(serializers.ModelSerializer):
    plannedMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = PlannedPM03
        fields = '__all__' 

class CompanyCodePPM03Serializer(serializers.ModelSerializer):
    plannedPM03List = PlannedPM03Serializer(many=True, read_only=True, source='plannedPM03_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM03List']



class ActualPM03Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM03
        fields = '__all__'

class CompanyCodeAPM03Serializer(serializers.ModelSerializer):
    actualPM03List = ActualPM03Serializer(many=True, read_only=True, source='actualPM03_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM03List']



class ActualPM04Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM04
        fields = '__all__'

class CompanyCodeAPM04Serializer(serializers.ModelSerializer):
    actualPM04List = ActualPM04Serializer(many=True, read_only=True, source='actualPM04_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM04List']



class PlannedPM05Serializer(serializers.ModelSerializer):
    plannedMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = PlannedPM03
        fields = '__all__' 
        
class CompanyCodePPM05Serializer(serializers.ModelSerializer):
    plannedPM05List = PlannedPM03Serializer(many=True, read_only=True, source='plannedPM05_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM05List']



class ActualPM05Serializer(serializers.ModelSerializer):
    actualMonth = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = ActualPM03
        fields = '__all__'
        
class CompanyCodeAPM05Serializer(serializers.ModelSerializer):
    actualPM05List = ActualPM04Serializer(many=True, read_only=True, source='actualPM05_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM05List']
