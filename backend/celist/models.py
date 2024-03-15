from django.db import models
from django.utils import timezone
from datetime import timedelta
from accounts.models import CompanyCode,CompanyName



class Plant(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='plant_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plant_companyName', null=True, blank=True)
    plant = plant = models.CharField(verbose_name='plant', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Plant'
        verbose_name_plural = 'Plant'
        ordering = ('plant',) 

    def __str__(self):
        return f'{self.plant}'




class Equipment(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='equipment_companyName', null=True, blank=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        ordering = ('companyCode',) 

    def __str__(self):
        return f'{self.equipment}'
    



class Machine(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='function_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='function_companyName', null=True, blank=True)
    machineName = models.CharField(verbose_name='machineName', max_length=200,null=True,blank=True)
    spareMachineLocationNo = models.CharField(verbose_name='spareMachineLocationNo', max_length=200,null=True,blank=True)#いつか設置されている場所を指定する場合のため

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machine'
        ordering = ('companyCode',) 

    def __str__(self):
        return f'{self.machineName}'




class TypeOfPM(models.Model):
     
    typeOfPM = models.CharField(verbose_name='typeOfPM',max_length=5,blank=True,null=True)
    description = models.TextField(verbose_name='PMDescription',blank=True,null=True,max_length=500)
    
    class Meta:
        verbose_name = 'TypeOfPM'
        verbose_name_plural = 'TypeOfPM'
        ordering = ('typeOfPM',) 
    def __str__(self):
        return f'{self.typeOfPM}'



class CeList(models.Model):

    #accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='ceList_companyCode',null=True, blank=True)
    
    #Celistメインの項目
    ceList_Id = models.CharField(verbose_name='ceListNo', max_length=200,null=True,blank=True,default=0)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='ceList_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='ceList_plant',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='ceList_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='ceList_machineName',null=True, blank=True)

    #Task List
    typeOfPM = models.ForeignKey(TypeOfPM, on_delete=models.PROTECT, related_name='ceList_typeOfPM',null=True, blank=True)#ここは絶対PROTECT
    taskName = models.CharField(verbose_name='taskName', max_length=200,null=True,blank=True,default=0)
 
    #Impact
    levelSetValue = models.PositiveIntegerField(verbose_name='levelSetValue', null=True,blank=True,default=0)
    mttr = models.PositiveSmallIntegerField(verbose_name='mttr',blank=True,null=True,default=0)
    possibilityOfProductionLv = models.CharField(verbose_name='possibilityOfProductionLv', max_length=200,null=True,blank=True)

    # Critical Equipment Level
    impactForProduction = models.CharField(verbose_name='impactForProduction', max_length=200, blank=True,null=True,)
    probabilityOfFailure = models.CharField(verbose_name='probabilityOfFailure', max_length=200, blank=True,null=True,)
    assessment = models.CharField(verbose_name='assessment', max_length=20, blank=True,null=True,)

    #Spare parts
    bomCode = models.CharField(verbose_name='bomCode', max_length=200,null=True,blank=True)
    #BomCost

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
   


class RepairingCostSum(models.Model):
    task = models.OneToOneField(TaskList, on_delete=models.CASCADE, related_name='repairing_cost_sum')
    repairingCost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_repairing_cost(self):
        task_cost = self.task.taskCost
        bom_cost = SpareParts.objects.get(bomCode=self.task.taskName).bomCost if SpareParts.objects.filter(bomCode=self.task.taskName).exists() else 0
        self.repairingCost = task_cost + bom_cost
        self.save()

    def __str__(self):
        return f'{self.task.taskName} - {self.repairingCost}'






