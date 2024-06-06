from django.db import models



class SimulationBenefit(models.Model):
  
  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
  
  class Meta:
    verbose_name = 'Equipment'
    verbose_name_plural = 'Equipment'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.equipment}'


class ImprovementBenefit(models.Model):

  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)

  class Meta:
    verbose_name = 'Equipment'
    verbose_name_plural = 'Equipment'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.equipment}'




class RiskAvoidBenefit(models.Model):
  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)

  class Meta:
    verbose_name = 'Equipment'
    verbose_name_plural = 'Equipment'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.equipment}'




class PartsManagementBenefit(models.Model):

    class Meta:
    verbose_name = 'Equipment'
    verbose_name_plural = 'Equipment'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.equipment}'
  
