from django.db import models
from django.utils import timezone
from datetime import timedelta
from accounts.models import Company,CompanyName

class Plant(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='plant_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plant_companyName', null=True, blank=True)
    plant = plant = models.CharField(verbose_name='plant', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plant'
        ordering = ('plant',) 

    def __str__(self):
        return f'{self.plant}'

class Equipment(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='equipment_companyName', null=True, blank=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        ordering = ('companyCode',) 

    def __str__(self):
        return f'{self.equipment}'
    


class Function(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='function_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='function_companyName', null=True, blank=True)
    function = models.CharField(verbose_name='function', max_length=200,null=True,blank=True)


class CeList(models.Model):

    #accountsから取得
    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='ceList_companyCode',null=True, blank=True)
    
    #Celistメインの項目
    #ceListId = models.CharField(verbose_name='ceListNo', max_length=200,null=True,blank=True,default=0)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='ceList_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='ceList_plant',null=True, blank=True)
    #plant = models.CharField(verbose_name='plant', max_length=200,null=True,blank=True)
    
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='ceList_equipment',null=True, blank=True)
    #equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)

    function = models.CharField(verbose_name='function', max_length=200,null=True,blank=True)
    locationNo = models.CharField(verbose_name='locationNo', max_length=200,null=True,blank=True)#いつか設置されている場所を指定する場合のため

    #Task List
    taskListCode = models.CharField(verbose_name='taskListNo', max_length=200,null=True,blank=True)

    #Impact
    levelSetValue = models.PositiveIntegerField(verbose_name='levelSetValue', null=True,blank=True,default=0)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr',blank=True,null=True,default=0)
    possibilityOfProductionLv = models.CharField(verbose_name='possibilityOfProductionLv', max_length=200,null=True,blank=True)

    # Critical Equipment Level
    impactForProduction = models.CharField(verbose_name='impactForProduction', max_length=200, blank=True,null=True,)
    probabilityOfFailure = models.CharField(verbose_name='probabilityOfFailure', max_length=200, blank=True,null=True,)
    assessment = models.CharField(verbose_name='assessment', max_length=20, blank=True,null=True,)

    #Spare parts
    bomCode = models.CharField(verbose_name='bomNo', max_length=200,null=True,blank=True)

    #Status of measures
    rcaOrReplace = models.BooleanField(verbose_name='rcaOrReplace',default=False)
    sparePartsOrAlternative = models.BooleanField(verbose_name='sparePartsOrAlternative',default=False)
    coveredFromTask = models.BooleanField(verbose_name='coveredFromTask',default=False)
    twoways = models.BooleanField(verbose_name='twoways',default=False)
    ceDescription = models.TextField(verbose_name='ceDescription',blank=True,null=True,max_length=1000)


    class Meta:
        verbose_name = 'Critical equipment list'
        verbose_name_plural = 'Critical equipment list'
        ordering = ('plant',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    
    def __str__(self):
        return f'{self.companyName}'
   








