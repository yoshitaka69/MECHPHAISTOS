from rest_framework import serializers
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05
from accounts.models import CompanyCode


class PlannedPM02Serializer(serializers.ModelSerializer):
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
    class Meta:
        model = ActualPM02
        fields = '__all__'

class CompanyCodeAPM02Serializer(serializers.ModelSerializer):
    actualPM02List = ActualPM02Serializer(many=True, read_only=True, source='actualPM02_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM02List']




class PlannedPM03Serializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedPM03
        fields = '__all__' 

class CompanyCodePPM03Serializer(serializers.ModelSerializer):
    plannedPM03List = PlannedPM03Serializer(many=True, read_only=True, source='plannedPM03_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM03List']



class ActualPM03Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM03
        fields = '__all__'

class CompanyCodeAPM03Serializer(serializers.ModelSerializer):
    actualPM03List = ActualPM03Serializer(many=True, read_only=True, source='actualPM03_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM03List']



class ActualPM04Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM04
        fields = '__all__'

class CompanyCodeAPM04Serializer(serializers.ModelSerializer):
    actualPM04List = ActualPM04Serializer(many=True, read_only=True, source='actualPM04_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM04List']



class PlannedPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedPM03
        fields = '__all__' 
        
class CompanyCodePPM05Serializer(serializers.ModelSerializer):
    plannedPM05List = PlannedPM03Serializer(many=True, read_only=True, source='plannedPM05_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM05List']



class ActualPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM03
        fields = '__all__'
        
class CompanyCodeAPM05Serializer(serializers.ModelSerializer):
    actualPM05List = ActualPM04Serializer(many=True, read_only=True, source='actualPM05_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM05List']



#ここからCalTable
#PM02
class CalTablePPM02Serializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedPM02
        fields = '__all__'
        
class CompanyCodeCalPPM02Serializer(serializers.ModelSerializer):
    calPPM02List = CalTablePPM02Serializer(many=True, read_only=True, source='calTablePlanPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM02List']



class CalTableAPM02Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM02
        fields = '__all__'
        
class CompanyCodeCalAPM02Serializer(serializers.ModelSerializer):
    calAPM02List = CalTableAPM02Serializer(many=True, read_only=True, source='calTableActualPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM02List']


#PM03
class CalTablePPM03Serializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedPM03
        fields = '__all__'
        
class CompanyCodeCalPPM03Serializer(serializers.ModelSerializer):
    calPPM03List = CalTablePPM03Serializer(many=True, read_only=True, source='calTablePlanPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM03List']



class CalTableAPM03Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM03
        fields = '__all__'
        
class CompanyCodeCalAPM03Serializer(serializers.ModelSerializer):
    calAPM03List = CalTableAPM03Serializer(many=True, read_only=True, source='calTableActualPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM03List']


#PM04
class CalTableAPM04Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM04
        fields = '__all__'
        
class CompanyCodeCalAPM04Serializer(serializers.ModelSerializer):
    calAPM04List = CalTableAPM04Serializer(many=True, read_only=True, source='calTableActualPM04_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM04List']


#PM05
class CalTablePPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = PlannedPM05
        fields = '__all__'
        
class CompanyCodeCalPPM05Serializer(serializers.ModelSerializer):
    calPPM05List = CalTablePPM05Serializer(many=True, read_only=True, source='calTablePlanPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM05List']


class CalTableAPM05Serializer(serializers.ModelSerializer):
    class Meta:
        model = ActualPM05
        fields = '__all__'
        
class CompanyCodeCalAPM05Serializer(serializers.ModelSerializer):
    calAPM05List = CalTableAPM05Serializer(many=True, read_only=True, source='calTableActualPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM05List']
