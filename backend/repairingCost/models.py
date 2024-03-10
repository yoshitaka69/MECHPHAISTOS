from django.db import models
from django.utils import timezone

from accounts.models import Company,CompanyName
from ceList.models import Plant

#RepairingCostPM02
class PlannedPM02(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='plannedPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plannedPM02_plant', null=True, blank=True)

    plannedPM02 = models.DecimalField(verbose_name='plannedPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now,null=True, blank=True)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1PlannedPM02 = models.DecimalField(verbose_name='no1PlannedPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalPlannedPM02 = models.DecimalField(verbose_name='totalPlannedPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM02'
        ordering = ('plant',)

    def __str__(self):
        return f'{self.plannedPM02}'



class ActualPM02(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='actualPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM02_plant', null=True, blank=True)

    actualPM02 = models.DecimalField(verbose_name='actualPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1ActualPM02 = models.DecimalField(verbose_name='no1ActualPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM02 = models.DecimalField(verbose_name='totalActualPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM02'
        ordering = ('plant',)

    def __str__(self):
        return f'{self.actualPM02}'
    


class PlannedPM03(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='plannedPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plannedPM03_plant', null=True, blank=True)

    plannedPM03 = models.DecimalField(verbose_name='plannedPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now,null=True, blank=True)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1PlannedPM03 = models.DecimalField(verbose_name='no1PlannedPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalPlannedPM03 = models.DecimalField(verbose_name='totalPlannedPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM03'
        ordering = ('plant',)

    def __str__(self):
        return f'{self.plannedPM03}'
    


class ActualPM03(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='actualPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM03_plant', null=True, blank=True)

    actualPM03 = models.DecimalField(verbose_name='actualPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1ActualPM03 = models.DecimalField(verbose_name='no1ActualPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM03 = models.DecimalField(verbose_name='totalActualPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM03'
        ordering = ('plant',)

    def __str__(self):
        return f'{self.actualPM03}'


class ActualPM04(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='actualPM04_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM04_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM04_plant', null=True, blank=True)

    actualPM04 = models.DecimalField(verbose_name='actualPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1ActualPM04 = models.DecimalField(verbose_name='no1ActualPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM04 = models.DecimalField(verbose_name='totalActualPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM04'
        ordering = ('plant',)
        
    def __str__(self):
        return f'{self.actualPM04}'


class PlannedPM05(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='plannedPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT,related_name='plannedPM05_plant', null=True, blank=True)
    
    plannedPM05 = models.DecimalField(verbose_name='plannedPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    plannedMonth = models.DateField(verbose_name='plannedMonth',default=timezone.now,null=True, blank=True)
    plannedCost = models.DecimalField(verbose_name='plannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1PlannedPM05 = models.DecimalField(verbose_name='no1PlannedPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalPlannedPM05 = models.DecimalField(verbose_name='totalPlannedPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM05'
        ordering = ('plant',)
        
    def __str__(self):
        return f'{self.plannedPM05}'

class ActualPM05(models.Model):

    companyCode = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='actualPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT,related_name='actualPM05_plant', null=True, blank=True)

    actualPM05 = models.DecimalField(verbose_name='actualPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    actualMonth = models.DateField(verbose_name='actualMonth',default=timezone.now,null=True, blank=True)
    actualCost = models.DecimalField(verbose_name='actualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1ActualPM05 = models.DecimalField(verbose_name='no1ActualPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM05 = models.DecimalField(verbose_name='totalActualPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM05'
        ordering = ('plant',)