from django.db import models
from django.utils import timezone

from accounts.models import CompanyCode,CompanyName
from ceList.models import Plant

#RepairingCostPM02
class PlannedPM02(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='plannedPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plannedPM02_plant', null=True, blank=True)

    #plannedPM02 = models.DecimalField(verbose_name='plannedPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now,null=True, blank=True)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM02'
        ordering = ('plant',)

    def __str__(self):
        return str('plannedPm02')



class ActualPM02(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM02_plant', null=True, blank=True)

    #actualPM02 = models.DecimalField(verbose_name='actualPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM02'
        ordering = ('plant',)

    def __str__(self):
        return str('actualPm02')
    


class PlannedPM03(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='plannedPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plannedPM03_plant', null=True, blank=True)

    #plannedPM03 = models.DecimalField(verbose_name='plannedPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now,null=True, blank=True)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM03'
        ordering = ('plant',)

    def __str__(self):
        return str('plannedPm03')
    


class ActualPM03(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM03_plant', null=True, blank=True)

    #actualPM03 = models.DecimalField(verbose_name='actualPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM03'
        ordering = ('plant',)

    def __str__(self):
        return str('actualPm03')


class ActualPM04(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM04_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM04_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM04_plant', null=True, blank=True)

    #actualPM04 = models.DecimalField(verbose_name='actualPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM04'
        ordering = ('plant',)
        
    def __str__(self):
        return str('actualPm04')


class PlannedPM05(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.PROTECT, related_name='plannedPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT,related_name='plannedPM05_plant', null=True, blank=True)
    
    #plannedPM05 = models.DecimalField(verbose_name='plannedPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now,null=True, blank=True)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM05'
        ordering = ('plant',)
        
    def __str__(self):
        return str('plannedPm05}')
    
class ActualPM05(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.PROTECT, related_name='actualPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT,related_name='actualPM05_plant', null=True, blank=True)

    #actualPM05 = models.DecimalField(verbose_name='actualPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM05'
        ordering = ('plant',)

    def __str__(self):
        return str('actualPm05')



class IndexFormPM02(models.Model):
    indexNamePM02 = models.CharField(verbose_name='indexNamePM02', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Index Form PM02'

    def __str__(self):
        return f'{self.indexNamePM02}'
    

class IndexFormPM03(models.Model):
    indexNamePM03 = models.CharField(verbose_name='indexNamePM03', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Index Form PM03'

    def __str__(self):
        return f'{self.indexNamePM03}'
    

class IndexFormPM04(models.Model):
    indexNamePM04 = models.CharField(verbose_name='indexNamePM04', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Index Form PM04'

    def __str__(self):
        return f'{self.indexNamePM04}'
    
class IndexFormPM05(models.Model):
    indexNamePM05 = models.CharField(verbose_name='indexNamePM05', max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Index Form PM05'

    def __str__(self):
        return f'{self.indexNamePM05}'




class CalculationTablePM02(models.Model):
    indexPM02 = models.DecimalField(verbose_name='indexPM2', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    cost = models.DecimalField(verbose_name='calCostPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePM02'

    def __str__(self):
        return f'{self.indexPM02}'


class CalculationTablePM03(models.Model):
    indexPM03 = models.DecimalField(verbose_name='indexPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    cost = models.DecimalField(verbose_name='calCostPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePM03'

    def __str__(self):
        return f'{self.indexPM03}'
    

class CalculationTablePM04(models.Model):
    indexPM04 = models.DecimalField(verbose_name='indexPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    cost = models.DecimalField(verbose_name='calCostPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePM04'

    def __str__(self):
        return f'{self.indexPM04}'


class CalculationTablePM05(models.Model):
    indexPM05 = models.DecimalField(verbose_name='indexPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    cost = models.DecimalField(verbose_name='calcCostPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePM05'

    def __str__(self):
        return f'{self.indexPM05}'

    

