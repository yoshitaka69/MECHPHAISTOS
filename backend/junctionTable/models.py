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


