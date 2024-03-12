from django.db import models
from django.utils import timezone

from accounts.models import CompanyCode,CompanyName
from ceList.models import Plant

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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM02'
        ordering = ('plant',)
    def __str__(self):
        return str('actualPm02')
    

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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM04'
        ordering = ('plant',)
        
    def __str__(self):
        return str('actualPm04')

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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
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
    commitment = models.DecimalField(verbose_name='commitment', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalCost = models.DecimalField(verbose_name='totalCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Repairing Cost Actual PM05'
        ordering = ('plant',)
    def __str__(self):
        return str('actualPm05')


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

