from django.db import models


class SimulationBenefit(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlannedPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlannedPM02_companyName', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)


    class Meta:
        verbose_name_plural = 'CalTablePlannedPM02'
        
    def __str__(self):
        return str('CalTablePlannedPM02')
