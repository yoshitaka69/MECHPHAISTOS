
from rest_framework import serializers
from .models import MasterDataTable,BomAndTask,CeListAndTask,BadActorManagement,EventYearPPM,GapOfRepairingCost
from taskList.models import TypicalTaskList,TaskListPPM02,TaskListPPM03,TaskListAPM04,TaskListPPM05
from spareParts.models import BomList
from accounts.models import CompanyCode,Plant
from ceList.models import Equipment, Machine




#-------------------------------------------------------------------------------------------------------------------------------------------------


from rest_framework import serializers
from .models import MasterDataTable, CompanyCode, Plant, Equipment, Machine, TypicalTaskList, BomList, TaskListPPM02, TaskListPPM03, TaskListAPM04

#ForeignKeyを文字列で返すslugフィールを関数化する。
def create_slug_related_field(field_name, queryset):
    return serializers.SlugRelatedField(
        slug_field=field_name, 
        queryset=queryset
    )

class MasterDataTableSerializer(serializers.ModelSerializer):
    companyCode = create_slug_related_field('companyCode', CompanyCode.objects.all())
    plant = create_slug_related_field('plant', Plant.objects.all())
    equipment = create_slug_related_field('equipment', Equipment.objects.all())
    machineName = create_slug_related_field('machineName', Machine.objects.all())

    typicalConstPeriod = create_slug_related_field('name', TypicalTaskList.objects.all())
    typicalTaskName = create_slug_related_field('typicalTaskName', TypicalTaskList.objects.all())
    typicalTaskCost = create_slug_related_field('cost', TypicalTaskList.objects.all())
    typicalNextEventDate = create_slug_related_field('nextEventDate', TypicalTaskList.objects.all())
    typicalSituation = create_slug_related_field('typicalSituation', TypicalTaskList.objects.all())

    bomCode = create_slug_related_field('bomCode', BomList.objects.all())
    bomStock = create_slug_related_field('stock', BomList.objects.all())
    maxPartsDeliveryTimeInBom = create_slug_related_field('maxDeliveryTime', BomList.objects.all())


    rcaOrReplace = serializers.BooleanField(required=False, allow_null=True)
    sparePartsOrAlternative = serializers.BooleanField(required=False, allow_null=True)
    coveredFromTask = serializers.BooleanField(required=False, allow_null=True)
    twoways = serializers.BooleanField(required=False, allow_null=True)

    class Meta:
        model = MasterDataTable
        fields = [
            "companyCode", 'ceListNo', 'plant', 'equipment', 'machineName', 'levelSetValue',
            'typicalConstPeriod', 'maxPartsDeliveryTimeInBom', 'mttr', 'possibilityOfContinuousProduction',
            'countOfPM02', 'latestPM02', 'countOfPM03', 'latestPM03', 'countOfPM04', 'latestPM04',
            'impactForProduction', 'probabilityOfFailure', 'assessment', 'typicalTaskName',
            'typicalTaskCost', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomStock',
            'rcaOrReplace', 'sparePartsOrAlternative', 'coveredFromTask', 'twoways', 'ceDescription'
        ]

    def create(self, validated_data):
        company_code_data = validated_data.pop('companyCode')
        instance = MasterDataTable.objects.create(companyCode=company_code_data, **validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.companyCode = validated_data.get('companyCode', instance.companyCode)
        instance.ceListNo = validated_data.get('ceListNo', instance.ceListNo)
        instance.plant = validated_data.get('plant', instance.plant)
        instance.equipment = validated_data.get('equipment', instance.equipment)
        instance.machineName = validated_data.get('machineName', instance.machineName)
        instance.levelSetValue = validated_data.get('levelSetValue', instance.levelSetValue)
        instance.typicalConstPeriod = validated_data.get('typicalConstPeriod', instance.typicalConstPeriod)
        instance.maxPartsDeliveryTimeInBom = validated_data.get('maxPartsDeliveryTimeInBom', instance.maxPartsDeliveryTimeInBom)
        instance.mttr = validated_data.get('mttr', instance.mttr)
        instance.possibilityOfContinuousProduction = validated_data.get('possibilityOfContinuousProduction', instance.possibilityOfContinuousProduction)
        instance.countOfPM02 = validated_data.get('countOfPM02', instance.countOfPM02)
        instance.latestPM02 = validated_data.get('latestPM02', instance.latestPM02)
        instance.countOfPM03 = validated_data.get('countOfPM03', instance.countOfPM03)
        instance.latestPM03 = validated_data.get('latestPM03', instance.latestPM03)
        instance.countOfPM04 = validated_data.get('countOfPM04', instance.countOfPM04)
        instance.latestPM04 = validated_data.get('latestPM04', instance.latestPM04)
        instance.impactForProduction = validated_data.get('impactForProduction', instance.impactForProduction)
        instance.probabilityOfFailure = validated_data.get('probabilityOfFailure', instance.probabilityOfFailure)
        instance.assessment = validated_data.get('assessment', instance.assessment)
        instance.typicalTaskName = validated_data.get('typicalTaskName', instance.typicalTaskName)
        instance.typicalTaskCost = validated_data.get('typicalTaskCost', instance.typicalTaskCost)
        instance.typicalNextEventDate = validated_data.get('typicalNextEventDate', instance.typicalNextEventDate)
        instance.typicalSituation = validated_data.get('typicalSituation', instance.typicalSituation)
        instance.bomCode = validated_data.get('bomCode', instance.bomCode)
        instance.bomStock = validated_data.get('bomStock', instance.bomStock)
        instance.rcaOrReplace = validated_data.get('rcaOrReplace', instance.rcaOrReplace)
        instance.sparePartsOrAlternative = validated_data.get('sparePartsOrAlternative', instance.sparePartsOrAlternative)
        instance.coveredFromTask = validated_data.get('coveredFromTask', instance.coveredFromTask)
        instance.twoways = validated_data.get('twoways', instance.twoways)
        instance.ceDescription = validated_data.get('ceDescription', instance.ceDescription)
        instance.save()
        return instance

class CompanyCodeMDTSerializer(serializers.ModelSerializer):
    MasterDataTable = MasterDataTableSerializer(many=True, read_only=True, source='masterDataTable_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'MasterDataTable']
    
    def create(self, validated_data):
        company_code_data = validated_data.pop('companyCode')
        instance = MasterDataTable.objects.create(companyCode=company_code_data, **validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.companyCode = validated_data.get('companyCode', instance.companyCode)
        instance.ceListNo = validated_data.get('ceListNo', instance.ceListNo)
        instance.save()
        return instance





#-------------------------------------------------------------------------------------------------------------------------------------------------



class BomAndTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BomAndTask
        fields = ['companyCode', 'companyName', 'plant', 'bomCode', 'taskCode', 'bomAndTaskSet', 'bomAndTaskSetCost']

class CompanyCodeBomAndTaskSerializer(serializers.ModelSerializer):
    BomAndTaskList = BomAndTaskSerializer(many=True, read_only=True, source='bomAndTask_companyCode')
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'BomAndTaskList']






class CeListAndTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CeListAndTask
        fields = ['companyCode', 'companyName', 'plant', 'equipment', 'no1HighLevelMachine', 'no1HighPriorityTaskName', 'no2HighLevelMachine', 'no2HighPriorityTaskName','no3HighLevelMachine', 'no3HighPriorityTaskName','no4HighLevelMachine', 'no4HighPriorityTaskName','no5HighLevelMachine', 'no5HighPriorityTaskName','no6HighLevelMachine', 'no6HighPriorityTaskName','no7HighLevelMachine', 'no7HighPriorityTaskName','no8HighLevelMachine', 'no8HighPriorityTaskName','no9HighLevelMachine', 'no9HighPriorityTaskName','no10HighLevelMachine', 'no10HighPriorityTaskName', 'no11HighLevelMachine', 'no11HighPriorityTaskName', 'no12HighLevelMachine', 'no12HighPriorityTaskName','no13HighLevelMachine', 'no13HighPriorityTaskName','no14HighLevelMachine', 'no14HighPriorityTaskName','no15HighLevelMachine', 'no15HighPriorityTaskName','no16HighLevelMachine', 'no16HighPriorityTaskName','no17HighLevelMachine', 'no17HighPriorityTaskName','no18HighLevelMachine', 'no18HighPriorityTaskName','no19HighLevelMachine', 'no19HighPriorityTaskName','no20HighLevelMachine', 'no20HighPriorityTaskName',]


class CompanyCodeCeListAndTaskSerializer(serializers.ModelSerializer):
    CeListAndTaskList = CeListAndTaskSerializer(many=True, read_only=True, source='ceListAndTask_companyCode')
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'CeListAndTaskList']





class BadActorManagementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BadActorManagement
        fields = ['companyCode', 'companyName', 'plant', 'equipment', 'badActor']

class CompanyCodeBadActorSerializer(serializers.ModelSerializer):
    BadActorList = BadActorManagementSerializer(many=True, read_only=True, source='badActorManagement_companyCode')
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'BadActorList']




class EventYearPPMSerializer(serializers.ModelSerializer):
    
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )
    
    class Meta:
        model = EventYearPPM
        fields = ['companyCode', 'companyName', 'plant', 'equipment', 'machine','PPM10YearCostAgo', 'PPM9YearCostAgo', 'PPM8YearCostAgo' ,'PPM7YearCostAgo' , 'PPM6YearCostAgo' ,'PPM5YearCostAgo', 'PPM4YearCostAgo', 'PPM3YearCostAgo', 'PPM2YearCostAgo', 'PPM1YearCostAgo', 'PPM10YearCost','PPM0YearCost', 'PPM1YearCost', 'PPM2YearCost' ,'PPM3YearCost' , 'PPM4YearCost' ,'PPM5YearCost', 'PPM6YearCost', 'PPM7YearCost', 'PPM8YearCost', 'PPM9YearCost', 'PPM10YearCost']

class CompanyCodeEventYearPPMSerializer(serializers.ModelSerializer):
    EventYearPPMList = EventYearPPMSerializer(many=True, read_only=True, source='eventYearPPM_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'EventYearPPMList']






class GapOfRepairingCostSerializer(serializers.ModelSerializer):
    
    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )
    
    class Meta:
        model = GapOfRepairingCost
        fields = ['companyCode', 'companyName', 'plant', 'equipment', 'machine', 'GapCostPPM10Ago', 'GapCostPPM9Ago', 'GapCostPPM8Ago', 'GapCostPPM7Ago', 'GapCostPPM6Ago', 'GapCostPPM5Ago', 'GapCostPPM4Ago', 'GapCostPPM3Ago', 'GapCostPPM2Ago', 'GapCostPPM1Ago', 'GapCostPPM0', 'GapCostPPM1', 'GapCostPPM2', 'GapCostPPM3', 'GapCostPPM4', 'GapCostPPM5', 'GapCostPPM6', 'GapCostPPM7', 'GapCostPPM8', 'GapCostPPM9', 'GapCostPPM10']

class CompanyCodeGapOfRepairingCostSerializer(serializers.ModelSerializer):
    GapOfRepairingCostList = GapOfRepairingCostSerializer(many=True, read_only=True, source='gapOfRepairingCost_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'GapOfRepairingCostList']
