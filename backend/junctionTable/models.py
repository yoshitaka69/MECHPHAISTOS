from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,CeList
from spareParts.models import BomList
from taskList.models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05


class MasterDataTable(models.Model):

    #accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='masterDataTable_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='masterDataTable_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='masterDataTable_plant',null=True, blank=True)

    #Celist
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='masterDataTable_equipment',null=True, blank=True)
    machineName = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='masterDataTable_machineName',null=True, blank=True)

    #TaskList
    taskPM02 = models.ForeignKey(TaskListPM02, on_delete=models.CASCADE, related_name='masterDataTable_taskPM02',null=True, blank=True)
    taskPM03 = models.ForeignKey(TaskListPM03, on_delete=models.CASCADE, related_name='masterDataTable_taskPM03',null=True, blank=True)
    taskPM04 = models.ForeignKey(TaskListPM04, on_delete=models.CASCADE, related_name='masterDataTable_taskPM04',null=True, blank=True)
    taskPM05 = models.ForeignKey(TaskListPM05, on_delete=models.CASCADE, related_name='masterDataTable_taskPM05',null=True, blank=True)
    multiTask = models.BooleanField(verbose_name='multiTask',default=False)

    #BomList
    bomCode = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='bomList_companyCode', null=True, blank=True)
    bomCost = models.DecimalField(verbose_name='bomCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    maxPartsDeliveryTimeInBom = models.PositiveIntegerField(verbose_name='maxPartsDeliveryTimeInBom', null=True,blank=True,default=0)


    #Impact
    levelSetValue = models.PositiveIntegerField(verbose_name='levelSetValue', null=True,blank=True,default=0)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr',blank=True,null=True,default=0)
    possibilityOfProductionLv = models.CharField(verbose_name='possibilityOfProductionLv', max_length=200,null=True,blank=True)

    # Critical Equipment Level
    impactForProduction = models.CharField(verbose_name='impactForProduction', max_length=200, blank=True,null=True,)
    probabilityOfFailure = models.CharField(verbose_name='probabilityOfFailure', max_length=200, blank=True,null=True,)
    assessment = models.CharField(verbose_name='assessment', max_length=20, blank=True,null=True,)

    #Status of measures
    rcaOrReplace = models.BooleanField(verbose_name='rcaOrReplace',default=False)
    sparePartsOrAlternative = models.BooleanField(verbose_name='sparePartsOrAlternative',default=False)
    coveredFromTask = models.BooleanField(verbose_name='coveredFromTask',default=False)
    twoways = models.BooleanField(verbose_name='twoways',default=False)
    ceDescription = models.TextField(verbose_name='ceDescription',blank=True,null=True,max_length=1000)


    #period of task
    thisYear10ago = models.BooleanField(verbose_name='thisYear10ago',default=False)
    thisYear9ago = models.BooleanField(verbose_name='thisYear9ago',default=False)
    thisYear8ago = models.BooleanField(verbose_name='thisYear8ago',default=False)
    thisYear7ago = models.BooleanField(verbose_name='thisYear7ago',default=False)
    thisYear6ago = models.BooleanField(verbose_name='thisYear6ago',default=False)
    thisYear5ago = models.BooleanField(verbose_name='thisYear5ago',default=False)
    thisYear4ago = models.BooleanField(verbose_name='thisYear4ago',default=False)
    thisYear3ago = models.BooleanField(verbose_name='thisYear3ago',default=False)
    thisYear2ago = models.BooleanField(verbose_name='thisYear2ago',default=False)
    thisYear1ago = models.BooleanField(verbose_name='thisYear1ago',default=False)
    thisYear = models.CharField(verbose_name='thisYear', max_length=200,blank=True,null=True)
    thisYear1later = models.BooleanField(verbose_name='thisYear1later',default=False)
    thisYear2later = models.BooleanField(verbose_name='thisYear2later',default=False)
    thisYear3later = models.BooleanField(verbose_name='thisYear3later',default=False)
    thisYear4later = models.BooleanField(verbose_name='thisYear4later',default=False)
    thisYear5later = models.BooleanField(verbose_name='thisYear5later',default=False)
    thisYear6later = models.BooleanField(verbose_name='thisYear6later',default=False)
    thisYear7later = models.BooleanField(verbose_name='thisYear7later',default=False)
    thisYear8later = models.BooleanField(verbose_name='thisYear8later',default=False)
    thisYear9later = models.BooleanField(verbose_name='thisYear9later',default=False)
    thisYear10later = models.BooleanField(verbose_name='thisYear10later',default=False)


def combine_and_save_to_master(task_pm02_instance, task_pm03_instance,):
    # データの取得
    data = {
        'thisYear1later': task_pm02_instance.thisYear1later or task_pm03_instance.thisYear1later,
        'thisYear2later': task_pm02_instance.thisYear2later or task_pm03_instance.thisYear2later,
        'thisYear3later': task_pm02_instance.thisYear3later or task_pm03_instance.thisYear3later,
        # ... その他のフィールドも同様に
        'thisYear10later': task_pm02_instance.thisYear10later or task_pm03_instance.thisYear10later,
    }

    # MasterDataTableに保存
    master_data_instance = MasterDataTable.objects.create(**data)
    return master_data_instance


