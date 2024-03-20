from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from ceList.models import Equipment,CeList
from spareParts.models import BomList
from taskList.models import TaskList


class MasterDataTable(models.Model):

    #accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='masterDataTable_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='masterDataTable_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='masterDataTable_plant',null=True, blank=True)

    #Celist
    ceList_Id = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='masterDataTable_ceList_Id',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='masterDataTable_equipment',null=True, blank=True)
    machineName = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='masterDataTable_machineName',null=True, blank=True)

    #TaskList
    taskCode = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_taskCode',null=True, blank=True)
    taskName = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_taskName',null=True, blank=True)
    typeOfPM = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_typeOfPM',null=True, blank=True)
    laborCostOfPM = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_countOfPM',null=True, blank=True)
    countOfPM = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_laborCostOfPM',null=True, blank=True)
    latestPM = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_latestPM',null=True, blank=True)
    periodOfPM = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_periodOfPM',null=True, blank=True)

    #BomList
    bomCode = models.ForeignKey(BomList, on_delete=models.CASCADE, related_name='bomList_companyCode', null=True, blank=True)
    bomCost = models.DecimalField(verbose_name='bomCost',max_digits=5,decimal_places=2,blank=True,null=True,default=0.00)
    maxPartsDeliveryTimeInBom = models.PositiveIntegerField(verbose_name='maxPartsDeliveryTimeInBom', null=True,blank=True,default=0)

    #TaskList  Probability of failure
    constructionPeriod = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_constructionPeriod',null=True, blank=True)
    nextEventDate = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_nextEventDate',null=True, blank=True)
    situation = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_situation',null=True, blank=True)

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


    #TaskList period of task
    thisYear10ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear10ago',null=True, blank=True)
    thisYear9ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear9ago',null=True, blank=True)
    thisYear8ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear8ago',null=True, blank=True)
    thisYear7ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear7ago',null=True, blank=True)
    thisYear6ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear6ago',null=True, blank=True)
    thisYear5ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear5ago',null=True, blank=True)
    thisYear4ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear4ago',null=True, blank=True)
    thisYear3ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear3ago',null=True, blank=True)
    thisYear2ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear2ago',null=True, blank=True)
    thisYear1ago = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear1ago',null=True, blank=True)
    thisYear = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear',null=True, blank=True)
    thisYear1later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear1later',null=True, blank=True)
    thisYear2later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear2later',null=True, blank=True)
    thisYear3later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear3later',null=True, blank=True)
    thisYear4later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear4later',null=True, blank=True)
    thisYear5later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear5later',null=True, blank=True)
    thisYear6later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear6later',null=True, blank=True)
    thisYear7later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear7later',null=True, blank=True)
    thisYear8later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear8later',null=True, blank=True)
    thisYear9later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear9later',null=True, blank=True)
    thisYear10later = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='masterDataTable_thisYear10later',null=True, blank=True)