from django.db import models
from django.utils import timezone

from accounts.models import CompanyCode,CompanyName,Plant


#RepairingCostPM02 項目が多くなるけど将来的にいろいろな企業が入ってきた際に、このように細かく振り分けておいたほうがわかり易くなるはず…
class PlannedPM02(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='plannedPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plannedPM02_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM02'
        ordering = ('plant',)
    def __str__(self):
        return str('plannedPm02')



class ActualPM02(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM02_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM02'
        ordering = ('plant',)
    def __str__(self):
        return str('actualPm02')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_summed_cost()

    



class PlannedPM03(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='plannedPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='plannedPM03_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM03'
        ordering = ('plant',)
    def __str__(self):
        return str('plannedPm03')
    



class ActualPM03(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM03_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM03'
        ordering = ('plant',)
    def __str__(self):
        return str('actualPm03')
    

class ActualPM04(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM04_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM04_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='actualPM04_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM04'
        ordering = ('plant',)
        
    def __str__(self):
        return str('actualPm04')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_summed_cost()



class PlannedPM05(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='plannedPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='plannedPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='plannedPM05_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Planned PM05'
        ordering = ('plant',)      
    def __str__(self):
        return str('plannedPm05}')


class ActualPM05(models.Model):

    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='actualPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='actualPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='actualPM05_plant', null=True, blank=True)

    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    jan = models.DecimalField(verbose_name='jan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    feb = models.DecimalField(verbose_name='feb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    mar = models.DecimalField(verbose_name='mar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    apr = models.DecimalField(verbose_name='apr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    may = models.DecimalField(verbose_name='may', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jun = models.DecimalField(verbose_name='jun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    jul = models.DecimalField(verbose_name='jul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    aug = models.DecimalField(verbose_name='aug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sep = models.DecimalField(verbose_name='sep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    oct = models.DecimalField(verbose_name='oct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    nov = models.DecimalField(verbose_name='nov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    dec = models.DecimalField(verbose_name='dec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    commitment = models.DecimalField(verbose_name='commitment(Unknown DeliveryTime)', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM05'
        ordering = ('plant',)
    def __str__(self):
        return str('actualPm05')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_summed_cost()



#項目が多くなるが、将来的にいろいろな企業が参加してくることを考慮し、ここは細かく設定するぞ！
class CalTablePlannedPM02(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlanPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlanPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTablePlanPM02_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePlanPm02'
    def __str__(self):
        return str('CalTablePlanPM02')


class CalTableActualPM02(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM02_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTableActualPM02'
    def __str__(self):
        return str('CalTableActualPM02')



class CalTablePlannedPM03(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlanPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlanPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTablePlanPM03_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePlanPm03'
    def __str__(self):
        return str('CalTablePlanPM03')


class CalTableActualPM03(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM03_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTableActualPM03'
    def __str__(self):
        return str('CalTableActualPM03')


class CalTableActualPM04(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM04_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM04_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM04_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTableActualPM04'
    def __str__(self):
        return str('CalTableActualPM04')



class CalTablePlannedPM05(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlanPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlanPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTablePlanPM05_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePlanPm05'
    def __str__(self):
        return str('CalTablePlanPM05')



class CalTableActualPM05(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM05_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTableActualPM05'
    def __str__(self):
        return str('CalTableActualPM05')



class SummedCost(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='summedCost_companyCode')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='summedCost_plant')

    # 各月の合計値
    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    sumJan = models.DecimalField(verbose_name='sumJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumFeb = models.DecimalField(verbose_name='sumFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumMar = models.DecimalField(verbose_name='sumMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumApr = models.DecimalField(verbose_name='sumApr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumMay = models.DecimalField(verbose_name='sumMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumJun = models.DecimalField(verbose_name='sumJun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumJul = models.DecimalField(verbose_name='sumJul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumAug = models.DecimalField(verbose_name='sumAug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumSep = models.DecimalField(verbose_name='sumSep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumOct = models.DecimalField(verbose_name='sumOct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumNov = models.DecimalField(verbose_name='sumNov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumDec = models.DecimalField(verbose_name='sumDec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumCommitment = models.DecimalField(verbose_name='sumCommit', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    totalActualPM02 = models.DecimalField(verbose_name='totalActualPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM03 = models.DecimalField(verbose_name='totalActualPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM04 = models.DecimalField(verbose_name='totalActualPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalActualPM05 = models.DecimalField(verbose_name='totalActualPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    totalActualCost = models.DecimalField(verbose_name='totalActualCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Total Actual Cost'
        ordering = ('plant',)
        
    def __str__(self):
        return f'{self.companyCode} {self.plant} {self.year}'
    
    def calculate_and_save_totals(self):
        # 各ActualPMモデルからデータを集計し、summed_costを更新するロジック
        total_cost_pm02 = self.calculate_total_for_model(ActualPM02, self.companyCode, self.plant, self.year)
        total_cost_pm03 = self.calculate_total_for_model(ActualPM03, self.companyCode, self.plant, self.year)
        total_cost_pm04 = self.calculate_total_for_model(ActualPM04, self.companyCode, self.plant, self.year)
        total_cost_pm05 = self.calculate_total_for_model(ActualPM05, self.companyCode, self.plant, self.year)
        # 各ActualPMモデルから得られた合計値を保存
        self.totalActualPM02 = total_cost_pm02
        self.totalActualPM03 = total_cost_pm03
        self.totalActualPM04 = total_cost_pm04
        self.totalActualPM05 = total_cost_pm05
        # インスタンスをデータベースに保存
        self.save()
    

    @classmethod
    def update_or_create_summed_cost(cls, company_code, plant, year):
        total_sum = {}

        # ActualPM02、ActualPM03、ActualPM04、ActualPM05 のデータを取得
        actualPM02 = ActualPM02.objects.filter(companyCode=company_code, plant=plant, year=year).first()
        actualPM03 = ActualPM03.objects.filter(companyCode=company_code, plant=plant, year=year).first()
        actualPM04 = ActualPM04.objects.filter(companyCode=company_code, plant=plant, year=year).first()
        actualPM05 = ActualPM05.objects.filter(companyCode=company_code, plant=plant, year=year).first()

        # 各PMモデルの合計値を計算
        total_sum['totalActualPM02'] = cls.calculate_total_for_model(ActualPM02, company_code, plant, year)
        total_sum['totalActualPM03'] = cls.calculate_total_for_model(ActualPM03, company_code, plant, year)
        total_sum['totalActualPM04'] = cls.calculate_total_for_model(ActualPM04, company_code, plant, year)
        total_sum['totalActualPM05'] = cls.calculate_total_for_model(ActualPM05, company_code, plant, year)

        # 各月の合計値を計算
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        for month in months:
            month_sum = sum(getattr(pm, month, 0) for pm in [actualPM02, actualPM03, actualPM04, actualPM05] if pm)
            total_sum[f'sum{month.capitalize()}'] = month_sum

        total_sum['sumCommitment'] = sum(getattr(pm, 'commitment', 0) for pm in [actualPM02, actualPM03, actualPM04, actualPM05] if pm)

        # SummedCost オブジェクトを作成または更新
        obj, created = cls.objects.update_or_create(
            companyCode=company_code, plant=plant, year=year,
            defaults=total_sum
        )
        return obj

    @classmethod
    def calculate_total_for_model(cls, model_class, company_code, plant, year):
        total_cost = 0
        model_instance = model_class.objects.filter(companyCode=company_code, plant=plant, year=year).first()
        if model_instance:
            total_cost += sum(getattr(model_instance, month, 0) for month in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
            total_cost += getattr(model_instance, 'commitment', 0)
        return total_cost
