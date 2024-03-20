from rest_framework import serializers
from accounts.models import CompanyCode
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05,CalTablePlannedPM02,CalTableActualPM02,CalTablePlannedPM03,CalTableActualPM03,CalTableActualPM04,CalTablePlannedPM05,CalTableActualPM05,SummedCost

from accounts.models import CompanyCode,Plant
from module.serializers import CommonSerializerMethodMixin


class PlannedPM02Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = PlannedPM02
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]
        
    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = PlannedPM02.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantPPM02Serializer(serializers.ModelSerializer):
    plannedPM02 = PlannedPM02Serializer(many=True, source='plannedPM02_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'plannedPM02']


class CompanyCodePPM02Serializer(serializers.ModelSerializer):
    plannedPM02List = PlantPPM02Serializer(many=True, read_only=True, source='plant_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った。

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM02List']







#Actual PM02 cost
class ActualPM02Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM02
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = ActualPM02.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantAPM02Serializer(serializers.ModelSerializer):
    actualPM02 = ActualPM02Serializer(many=True, source='actualPM02_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM02']
    

class CompanyCodeAPM02Serializer(serializers.ModelSerializer):
    actualPM02List =PlantAPM02Serializer(many=True, read_only=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM02List']








#plannedPM03
class PlannedPM03Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlannedPM03
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]
        
    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = PlannedPM03.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantPPM03Serializer(serializers.ModelSerializer):
    plannedPM03 = PlannedPM03Serializer(many=True, source='plannedPM03_plant') 

    class Meta:
        model = Plant
        fields = ['plant', 'plannedPM03']


class CompanyCodePPM03Serializer(serializers.ModelSerializer):
    plannedPM03List = PlantPPM03Serializer(many=True, read_only=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM03List']






#PM03-actual
class ActualPM03Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM03
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = ActualPM03.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantAPM03Serializer(serializers.ModelSerializer):
    actualPM03 = ActualPM02Serializer(many=True, source='actualPM03_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM03']
    

class CompanyCodeAPM03Serializer(serializers.ModelSerializer):
    actualPM03List =PlantAPM03Serializer(many=True, read_only=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM03List']






#PM04-actual
class ActualPM04Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM04
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = ActualPM04.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantAPM04Serializer(serializers.ModelSerializer):
    actualPM04 = ActualPM04Serializer(many=True, source='actualPM04_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM04']
    

class CompanyCodeAPM04Serializer(serializers.ModelSerializer):
    actualPM04List =PlantAPM04Serializer(many=True, read_only=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM04List']







class PlannedPM05Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlannedPM05
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]
        
    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = PlannedPM05.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantPPM05Serializer(serializers.ModelSerializer):
    plannedPM05 = PlannedPM05Serializer(many=True, source='plannedPM05_plant') 

    class Meta:
        model = Plant
        fields = ['plant', 'plannedPM05']


class CompanyCodePPM05Serializer(serializers.ModelSerializer):
    plannedPM05List = PlantPPM05Serializer(many=True, read_only=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM05List']






#PM05^actual
class ActualPM05Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM05
        fields = ['companyCode','plant','year','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec','commitment','totalCost',]


    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # companyCode、plant、年を取得
        company_code = validated_data.get('companyCode')
        plant = validated_data.get('plant')
        year = validated_data.get('year')

        # 既存のレコードを検索
        existing_record = ActualPM05.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        if existing_record:
            # 既存のレコードが存在する場合は、そのレコードを更新
            return self.update(existing_record, validated_data)
        else:
            # 既存のレコードが存在しない場合は、新しいレコードを作成
            return super().create(validated_data)

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance

class PlantAPM05Serializer(serializers.ModelSerializer):
    actualPM05 = ActualPM05Serializer(many=True, source='actualPM05_plant')  # Co2 モデルの related_name

    class Meta:
        model = Plant
        fields = ['plant', 'actualPM05']
    

class CompanyCodeAPM05Serializer(serializers.ModelSerializer):
    actualPM05List =PlantAPM05Serializer(many=True, read_only=True, source='plant_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM05List']







#ここからCalTable
#PM02
class CalTablePPM02Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTablePlannedPM02
        fields = '__all__'

        
class CompanyCodeCalPPM02Serializer(serializers.ModelSerializer):
    calPPM02List = CalTablePPM02Serializer(many=True, read_only=True, source='calTablePlanPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM02List']



class CalTableAPM02Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTableActualPM02
        fields = '__all__'



class CompanyCodeCalAPM02Serializer(serializers.ModelSerializer):
    calAPM02List = CalTableAPM02Serializer(many=True, read_only=True, source='calTableActualPM02_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM02List']




#PM03
class CalTablePPM03Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTablePlannedPM03
        fields = '__all__'

        
        
class CompanyCodeCalPPM03Serializer(serializers.ModelSerializer):
    calPPM03List = CalTablePPM03Serializer(many=True, read_only=True, source='calTablePlanPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM03List']





class CalTableAPM03Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()

    class Meta:
        model = CalTableActualPM03
        fields = '__all__'

        
class CompanyCodeCalAPM03Serializer(serializers.ModelSerializer):
    calAPM03List = CalTableAPM03Serializer(many=True, read_only=True, source='calTableActualPM03_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM03List']




#PM04
class CalTableAPM04Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTableActualPM04
        fields = '__all__'

        
class CompanyCodeCalPPM04Serializer(serializers.ModelSerializer):
    calPPM04List = CalTableAPM04Serializer(many=True, read_only=True, source='calTablePlanPM04_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM04List']




class CalTablePPM05Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTablePlannedPM05
        fields = '__all__'


class CompanyCodeCalPPM05Serializer(serializers.ModelSerializer):
    calPPM05List = CalTablePPM05Serializer(many=True, read_only=True, source='calTablePlannedPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calPPM05List']





class CalTableAPM05Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()
    
    class Meta:
        model = CalTableActualPM05
        fields = '__all__'


class CompanyCodeCalAPM05Serializer(serializers.ModelSerializer):
    calAPM05List = CalTableAPM05Serializer(many=True, read_only=True, source='calTableActualPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM05List']





class SummedCostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SummedCost
        fields = '__all__'

class CompanyCodeSummedCostSerializer(serializers.ModelSerializer):
    summedCostList = SummedCostSerializer(many=True, read_only=True, source='summedCost_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'summedCostList']