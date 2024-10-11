
from rest_framework import serializers
from .models import MasterDataTable,BomAndTask,CeListAndTask,BadActorManagement,EventYearPPM,GapOfRepairingCost
from taskList.models import TypicalTaskList,TaskListPPM02,TaskListPPM03,TaskListAPM04,TaskListPPM05
from spareParts.models import BomList
from accounts.models import CompanyCode,Plant
from ceList.models import Equipment, Machine




#-------------------------------------------------------------------------------------------------------------------------------------------------


from rest_framework import serializers
from .models import MasterDataTable, CompanyCode, Plant, Equipment, Machine, TypicalTaskList, BomList, TaskListPPM02, TaskListPPM03, TaskListAPM04



class MasterDataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterDataTable
        fields = '__all__'



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





#-------------------------------------------------------------------------------------------------------------------------------------------------


from rest_framework import serializers
from .models import CeListAndTask

class CeListAndTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CeListAndTask
        # No.1～No.20までの全フィールドをリストに追加
        fields = [
            'companyCode', 'companyName',
            *[f'no{i}Plant' for i in range(1, 21)],
            *[f'no{i}HighLevelMachine' for i in range(1, 21)],
            *[f'no{i}HighPriorityTaskName' for i in range(1, 21)],
            *[f'no{i}Equipment' for i in range(1, 21)],
            *[f'no{i}PMType' for i in range(1, 21)],
            *[f'no{i}Cost' for i in range(1, 21)],
            *[f'no{i}Assessment' for i in range(1, 21)],
        ]


class CompanyCodeCeListAndTaskSerializer(serializers.ModelSerializer):
    CeListAndTaskList = CeListAndTaskSerializer(many=True, read_only=True, source='ceListAndTask_companyCode')
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'CeListAndTaskList']


#-------------------------------------------------------------------------------------------------------------------------------------------------




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






#scheduleForCalendarモデル
#----------------------------------------------------------------------------------------------------------------------------------------------
from rest_framework import serializers
from .models import ScheduleForGantt

class ScheduleForGanttSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleForGantt
        fields = '__all__'  # すべてのフィールドを自動的にシリアライズ

class CompanyCodeScheduleForGanttSerializer(serializers.ModelSerializer):
    ScheduleForGanttList = ScheduleForGanttSerializer(many=True, read_only=True, source='scheduleForGantt_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ScheduleForGanttList']






#----------------------------------------------------------------------------------------------------------------------------------------------


from rest_framework import serializers
from .models import ScheduleForCalendar

class ScheduleForCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleForCalendar
        fields = '__all__'  # 必要なフィールドが含まれていることを確認


class CompanyCodeScheduleForCalendarSerializer(serializers.ModelSerializer):
    ScheduleForCalendarList = ScheduleForCalendarSerializer(many=True, read_only=True, source='scheduleForCalendar_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ScheduleForCalendarList']
        

#----------------------------------------------------------------------------------------------------------------------------------------------