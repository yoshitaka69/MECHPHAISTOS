from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant


class Equipment(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='equipment_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='equipment_plant',null=True, blank=True)
    equipment = models.CharField(verbose_name='equipment', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        ordering = ('companyCode',) 

    def __str__(self):
        return f'{self.equipment}'
    

class Machine(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='machine_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='machine_companyName', null=True, blank=True)
    machineName = models.CharField(verbose_name='machineName', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machine'
        ordering = ('companyCode',) 

    def __str__(self):
        return f'{self.machineName}'
    

class CeList(models.Model):

    #accountsから取得
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='ceList_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='ceList_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='ceList_plant',null=True, blank=True)
    
    #Celistの項目
    ceListNo = models.CharField(verbose_name='ceListNo', max_length=200,null=True,blank=True,default=0)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='ceList_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='ceList_machine',null=True, blank=True)
 
    class Meta:
        verbose_name = 'Critical equipment list'
        verbose_name_plural = 'Critical equipment list'
        ordering = ('plant',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('CeList')



class RiskMatrixPossibility(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='riskMatrixPossibility_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='riskMatrixPossibility_companyName', null=True, blank=True)
    x = models.FloatField(verbose_name='x', blank=True, null=True, default=0)
    y = models.FloatField(verbose_name='y', blank=True, null=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Risk Matrix Possibility'
        verbose_name_plural = 'Risk Matrix Possibility'
        ordering = ('-timestamp',)

    def __str__(self):
        return f'CompanyCode: {self.companyCode}, x: {self.x}, y: {self.y}'




class RiskMatrixImpact(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='riskMatrixImpact_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='riskMatrixImpact_companyName', null=True, blank=True)
    levelSetValue = models.CharField(verbose_name='levelSetValue', max_length=200,null=True,blank=True)
    x = models.FloatField(verbose_name='x', blank=True, null=True, default=0)
    y = models.FloatField(verbose_name='y', blank=True, null=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Risk Matrix Impact'
        verbose_name_plural = 'Risk Matrix Impact'
        ordering = ('-timestamp',)

    def __str__(self):
        return f'CompanyCode: {self.companyCode}, x: {self.x}, y: {self.y}'