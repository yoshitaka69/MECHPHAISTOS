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
    plant = models.CharField(verbose_name='plant', max_length=100, null=True, blank=True)

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
    plant = models.CharField(verbose_name='plant', max_length=100, null=True, blank=True)

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
    plant = models.CharField(verbose_name='plant', max_length=100, null=True, blank=True)

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
    plant = models.CharField(verbose_name='plant', max_length=100, null=True, blank=True)

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


  


