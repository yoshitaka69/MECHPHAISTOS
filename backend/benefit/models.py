from django.db import models



class SimulationBenefit(models.Model):
  
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


class ImprovementBenefit(models.Model):

  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)



class RiskAvoidBenefit(models.Model):
  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)


class PartsManagementBenefit(models.Model):
  
