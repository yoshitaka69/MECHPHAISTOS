from django.db import models



class SimulationBenefit(models.Model):
  
  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='simulationBenefit_companyCode',null=True, blank=True)
  janSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  febSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  marSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  aprSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  maySB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  junSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  julSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  augSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  sepSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  octSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  novSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  decSB  = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear1Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear2Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear3Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear4Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear5Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear6Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear7Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear8Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear9Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  thisYear10Later = models.DecimalField(verbose_name='janSB', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
  class Meta:
    verbose_name = 'SimulationBenefit'
    verbose_name_plural = 'SimulationBenefit'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.SimulationBenefit}'




class ImprovementBenefit(models.Model):

  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
  improvementBenefit = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)

  class Meta:
    verbose_name = 'Improvement Benefit'
    verbose_name_plural = 'Improvement Benefit'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.improvementBenefit}'




class RiskAvoidBenefit(models.Model):
  
  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
  RiskAvoidBenefit = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)

  class Meta:
    verbose_name = 'RiskAvoidBenefit'
    verbose_name_plural = 'RiskAvoidBenefit'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.riskAvoidBenefit}'




class PartsManagementBenefit(models.Model):
  
  companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)
  PartsManagementBenefit = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='equipment_companyCode',null=True, blank=True)

    class Meta:
    verbose_name = 'partsManagementBenefit'
    verbose_name_plural = 'partsManagementBenefit'
    ordering = ('companyCode',) 
    
    def __str__(self):
      return f'{self.partsManagementBenefit}'
  
