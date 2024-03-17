from rest_framework import serializers
from accounts.models import CompanyCode
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05,CalTablePlannedPM02,CalTableActualPM02,CalTablePlannedPM03,CalTableActualPM03,CalTableActualPM04,CalTablePlannedPM05,CalTableActualPM05

from accounts.models import CompanyCode,Plant
from taskList.models import TaskList
from module.serializers import CommonSerializerMethodMixin


class PlannedPM02Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = PlannedPM02
        fields = '__all__'
        
    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # createのロジック...
        instance = super().create(validated_data)
        self.save_total_cost(instance)
        return instance

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance


class CompanyCodePPM02Serializer(serializers.ModelSerializer):
    plannedPM02List = PlannedPM02Serializer(many=True, read_only=True, source='plannedPM02_companyCode')#sourceはmodelのrelated_nameにすること。ここで嵌った。

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









class PlannedPM03Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlannedPM03
        fields = '__all__' 


    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # createのロジック...
        instance = super().create(validated_data)
        self.save_total_cost(instance)
        return instance

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance


class CompanyCodePPM03Serializer(serializers.ModelSerializer):
    plannedPM03List = PlannedPM03Serializer(many=True, read_only=True, source='plannedPM03_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM03List']







class ActualPM03Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM03
        fields = '__all__'

    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # createのロジック...
        instance = super().create(validated_data)
        self.save_total_cost(instance)
        return instance

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance



class CompanyCodeAPM03Serializer(serializers.ModelSerializer):
    actualPM03List = ActualPM03Serializer(many=True, read_only=True, source='actualPM03_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM03List']






class ActualPM04Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM04
        fields = '__all__'


    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # createのロジック...
        instance = super().create(validated_data)
        self.save_total_cost(instance)
        return instance

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance
    

class CompanyCodeAPM04Serializer(serializers.ModelSerializer):
    actualPM04List = ActualPM04Serializer(many=True, read_only=True, source='actualPM04_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'actualPM04List']






class PlannedPM05Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PlannedPM05
        fields = '__all__' 

    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # createのロジック...
        instance = super().create(validated_data)
        self.save_total_cost(instance)
        return instance

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance
    
        
class CompanyCodePPM05Serializer(serializers.ModelSerializer):
    plannedPM05List = PlannedPM03Serializer(many=True, read_only=True, source='plannedPM05_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'plannedPM05List']






class ActualPM05Serializer(CommonSerializerMethodMixin,serializers.ModelSerializer):
    totalCost = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ActualPM05
        fields = '__all__'

    # createとupdateメソッドで共通ロジックを呼び出す
    def create(self, validated_data):
        # createのロジック...
        instance = super().create(validated_data)
        self.save_total_cost(instance)
        return instance

    def update(self, instance, validated_data):
        # updateのロジック...
        instance = super().update(instance, validated_data)
        self.save_total_cost(instance)
        return instance
        
class CompanyCodeAPM05Serializer(serializers.ModelSerializer):
    actualPM05List = ActualPM04Serializer(many=True, read_only=True, source='actualPM05_companyCode')

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


    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None


    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)

        
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
        
    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None

        

    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)




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

    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None


    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)

        
        
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

        
    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None


    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)

        
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

    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None


    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)


        
class CompanyCodeCalAPM04Serializer(serializers.ModelSerializer):
    calAPM04List = CalTableAPM04Serializer(many=True, read_only=True, source='calTableActualPM04_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM04List']





#PM05
class CalTablePPM05Serializer(serializers.ModelSerializer):
    no1RepairingCost = serializers.SerializerMethodField()
    no2RepairingCost = serializers.SerializerMethodField()
    no3RepairingCost = serializers.SerializerMethodField()
    no4RepairingCost = serializers.SerializerMethodField()
    no5RepairingCost = serializers.SerializerMethodField()

    class Meta:
        model = CalTablePlannedPM05
        fields = '__all__'

    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None

        
    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)

        
class CompanyCodeCalPPM05Serializer(serializers.ModelSerializer):
    calPPM05List = CalTablePPM05Serializer(many=True, read_only=True, source='calTablePlanPM05_companyCode')
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

    def get_repairing_cost_info(self, rank):
        try:
            task_list = TaskList.objects.order_by('-laborCostOfPM')[:5]  # laborCostOfPMで降順にソートし、上位5位までを取得
            if len(task_list) > rank:
                task = task_list[rank]
                return {'taskName': task.taskName, 'repairingCost': task.laborCostOfPM}
            return None
        except Exception as e:
            # 例外が発生した場合、エラーログを記録する
            print(f'Error in get_repairing_cost_info: {e}')
            return None


    def get_no1RepairingCost(self, obj):
        return self.get_repairing_cost_info(0)

    def get_no2RepairingCost(self, obj):
        return self.get_repairing_cost_info(1)

    def get_no3RepairingCost(self, obj):
        return self.get_repairing_cost_info(2)

    def get_no4RepairingCost(self, obj):
        return self.get_repairing_cost_info(3)

    def get_no5RepairingCost(self, obj):
        return self.get_repairing_cost_info(4)



class CompanyCodeCalAPM05Serializer(serializers.ModelSerializer):
    calAPM05List = CalTableAPM05Serializer(many=True, read_only=True, source='calTableActualPM05_companyCode')
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'calAPM05List']
