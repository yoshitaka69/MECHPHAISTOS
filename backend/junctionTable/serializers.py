from rest_framework import serializers
from .models import MasterDataTable,BomAndTask,AlertSchedule
from taskList.models import TypicalTaskList,TaskListPPM02,TaskListPPM03,TaskListAPM04,TaskListPPM05
from spareParts.models import BomList
from accounts.models import CompanyCode,Plant
from ceList.models import Equipment, Machine



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

    typicalConstPeriod = create_slug_related_field('typicalConstPeriod', TypicalTaskList.objects.all())
    #typicalLatestDate = create_slug_related_field('typicalLatestDate', TypicalTaskList.objects.all())
    typicalTaskName = create_slug_related_field('typicalTaskName', TypicalTaskList.objects.all())
    typicalTaskCost = create_slug_related_field('typicalTaskCost', TypicalTaskList.objects.all())
    
    #multiTasking = create_slug_related_field('multiTasking', TypicalTaskList.objects.all())
    typicalNextEventDate = create_slug_related_field('typicalNextEventDate', TypicalTaskList.objects.all())
    typicalSituation = create_slug_related_field('typicalSituation', TypicalTaskList.objects.all())

    bomCode = create_slug_related_field('bomCode', BomList.objects.all())
    #bomCost = create_slug_related_field('bomCost', BomList.objects.all())
    maxPartsDeliveryTimeInBom = create_slug_related_field('maxPartsDeliveryTimeInBom', BomList.objects.all())

    countOfPM02 = create_slug_related_field('countOfPM02', TaskListPPM02.objects.all())
    latestPM02 = create_slug_related_field('latestPM02', TaskListPPM02.objects.all())
    countOfPM03 = create_slug_related_field('countOfPM03', TaskListPPM03.objects.all())
    latestPM03 = create_slug_related_field('latestPM03', TaskListPPM03.objects.all())
    countOfPM04 = create_slug_related_field('countOfPM04', TaskListAPM04.objects.all())
    latestPM04 = create_slug_related_field('latestPM04', TaskListAPM04.objects.all())



    
    class Meta:
        model = MasterDataTable #呼び出すモデル名
        fields = ["companyCode", 'ceListNo', 'plant', 'equipment', 'machineName', 'levelSetValue', 'typicalConstPeriod', 'maxPartsDeliveryTimeInBom', 'mttr', 'probabilityOfFailure', 'countOfPM02', 'latestPM02', 'countOfPM03', 'latestPM03', 'countOfPM04', 'latestPM04', 'impactForProduction', 'probabilityOfFailure', 'assessment', 'typicalTaskName', 'typicalTaskCost', 'typicalConstPeriod', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomStock', 'rcaOrReplace', 'sparePartsOrAlternative', 'coveredFromTask', 'twoways', 'ceDescription']# API上に表示するモデルのデータ項目


class CompanyCodeMDTSerializer(serializers.ModelSerializer):
    MasterDataTable = MasterDataTableSerializer(many=True, read_only=True, source='masterDataTable_companyCode')#ここのsourceは注意

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'MasterDataTable']







class BomAndTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BomAndTask
        field = ['companyCode', 'companyName', 'plant', 'bomCode', 'taskCode', 'bomAndTaskSet', 'bomAndTaskSetCost']

class CompanyCodeBomAndTaskSerializer(serializers.ModelSerializer):
    BomAndTaskList = BomAndTaskSerializer(many=True, read_only=True, source='bomAndTask_companyCode')
    
    class Meta:
        model = CompanyCode
        field = ['companyCode', 'BomAndTaskList']







class AlertScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertSchedule
        field = ['companyCode', 'companyName', 'plant', 'nextMonthTaskAlert']

class CompanyCodeAlertScheduleSerializer(serializers.ModelSerializer):
    AlertScheduleList = AlertScheduleSerializer(many=True, read_only=True, source='alertSchedule_companyCode')
    
    class Meta:
        model = CompanyCode
        field = ['companyCode', 'AlertScheduleList']



    
