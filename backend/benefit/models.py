from django.db import models

class PlanOptimizationBenefit(models.Model):

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='planOptimizationBenefit_companyCode',null=True, blank=True)

    benefitJan = models.DecimalField(verbose_name='sumJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitFeb = models.DecimalField(verbose_name='sumFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitMar = models.DecimalField(verbose_name='sumMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitApr = models.DecimalField(verbose_name='sumApr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitMay = models.DecimalField(verbose_name='sumMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitJun = models.DecimalField(verbose_name='sumJun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitJul = models.DecimalField(verbose_name='sumJul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitAug = models.DecimalField(verbose_name='sumAug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitSep = models.DecimalField(verbose_name='sumSep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitOct = models.DecimalField(verbose_name='sumOct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitNov = models.DecimalField(verbose_name='sumNov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    benefitDec = models.DecimalField(verbose_name='sumDec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'Plan Optimization Benefit'
        verbose_name_plural = 'Plan Optimization Benefit'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"
    
