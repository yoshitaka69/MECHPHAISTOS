from rest_framework import serializers
from .models import MasterDataTable
from taskList.models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05
from spareParts.models import BomList
from accounts.models import CompanyCode

class TaskListPM02MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskListPM02 #呼び出すモデル名
        fields = ['companyCode','companyName','plant','equipment','machineName','taskCode','taskName','laborCostOfPM','countOfPM','latestPM','periodOfPM','constructionPeriod','nextEventDate','situation','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',]# API上に表示するモデルのデータ項目


class TaskListPM03MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskListPM03 #呼び出すモデル名
        fields = ['companyCode','companyName','plant','equipment','machineName','taskCode','taskName','laborCostOfPM','countOfPM','latestPM','periodOfPM','constructionPeriod','nextEventDate','situation','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',]# API上に表示するモデルのデータ項目


class TaskListPM04MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskListPM04 #呼び出すモデル名
        fields = ["companyCode","companyName","plant","equipment","machineName","taskCode","taskName","laborCostOfPM","countOfPM","latestPM","constructionPeriod",]# API上に表示するモデルのデータ項目


class TaskListPM05MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskListPM05 #呼び出すモデル名
        fields = ['companyCode','companyName','plant','equipment','machineName','taskCode','taskName','laborCostOfPM','countOfPM','latestPM','periodOfPM','constructionPeriod','nextEventDate','situation','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',]# API上に表示するモデルのデータ項目


class BomListMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = BomList #呼び出すモデル名
        fields = ['bomCode','bomCost',]# API上に表示するモデルのデータ項目




class MasterDataTableSerializer(serializers.ModelSerializer):
    taskPM02List = TaskListPM02MasterSerializer(source='taskPM02')#ここのsourceは本当に注意
    taskPM03List = TaskListPM03MasterSerializer(source='taskPM03')#ここのsourceは本当に注意
    taskPM04List = TaskListPM04MasterSerializer(source='taskPM04')#ここのsourceは本当に注意
    taskPM05List = TaskListPM05MasterSerializer(source='taskPM05')#ここのsourceは本当に注意

    bomCodeList = BomListMasterSerializer(source='bomCode')#ここのsourceは本当に注意


    class Meta:
        model = MasterDataTable #呼び出すモデル名
        fields = ['companyCode','companyName','plant','equipment','machineName','taskPM02List','taskPM03List','taskPM04List','taskPM05List','multiTask','bomCodeList','bomCost','maxPartsDeliveryTimeInBom','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription']# API上に表示するモデルのデータ項目


class CompanyCodeMDTSerializer(serializers.ModelSerializer):
    masterDataTableList = MasterDataTableSerializer(many=True, read_only=True, source='masterDataTable_companyCode')#ここのsourceは本当に注意
    
    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'masterDataTableList']

