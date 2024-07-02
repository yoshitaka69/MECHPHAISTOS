from django.db import models

class PlanOptimizationBenefit(models.Model):

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='planOptimizationBenefit_companyCode',null=True, blank=True)

    planOptJan = models.DecimalField(verbose_name='planOptJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptFeb = models.DecimalField(verbose_name='planOptFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptMar = models.DecimalField(verbose_name='planOptMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptApr = models.DecimalField(verbose_name='planOptApr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptMay = models.DecimalField(verbose_name='planOptMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptJun = models.DecimalField(verbose_name='planOptJun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptJul = models.DecimalField(verbose_name='planOptJul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptAug = models.DecimalField(verbose_name='planOptAug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptSep = models.DecimalField(verbose_name='planOptSep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptOct = models.DecimalField(verbose_name='planOptOct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptNov = models.DecimalField(verbose_name='planOptNov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    planOptDec = models.DecimalField(verbose_name='planOptDec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'Plan Optimization Benefit'
        verbose_name_plural = 'Plan Optimization Benefit'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"
    


class ImprovementBenefit(models.Model):

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='planOptimizationBenefit_companyCode',null=True, blank=True)

    improvementJan = models.DecimalField(verbose_name='improvementJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementFeb = models.DecimalField(verbose_name='improvementFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementMar = models.DecimalField(verbose_name='improvementMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementApr = models.DecimalField(verbose_name='improvementApr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementMay = models.DecimalField(verbose_name='improvementMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementJun = models.DecimalField(verbose_name='improvementJun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementJul = models.DecimalField(verbose_name='improvementJul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementAug = models.DecimalField(verbose_name='improvementAug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementSep = models.DecimalField(verbose_name='improvementSep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementOct = models.DecimalField(verbose_name='improvementOct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementNov = models.DecimalField(verbose_name='improvementNov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    improvementDec = models.DecimalField(verbose_name='improvementDec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'Improvement Benefit'
        verbose_name_plural = 'Improvement Benefit'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"


class riskAvoidanceBenefit(models.Model):

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='planOptimizationBenefit_companyCode',null=True, blank=True)

    riskAvoidJan = models.DecimalField(verbose_name='riskAvoidJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidFeb = models.DecimalField(verbose_name='riskAvoidFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidMar = models.DecimalField(verbose_name='riskAvoidMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidApr = models.DecimalField(verbose_name='riskAvoidApr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidMay = models.DecimalField(verbose_name='riskAvoidMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidJun = models.DecimalField(verbose_name='riskAvoidJun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidJul = models.DecimalField(verbose_name='riskAvoidJul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidAug = models.DecimalField(verbose_name='riskAvoidAug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidSep = models.DecimalField(verbose_name='riskAvoidSep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidOct = models.DecimalField(verbose_name='riskAvoidOct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidNov = models.DecimalField(verbose_name='riskAvoidNov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    riskAvoidDec = models.DecimalField(verbose_name='riskAvoidDec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'risk Avoidance Benefit'
        verbose_name_plural = 'risk Avoidance Benefit'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"



class vendorSelectionBenefit(models.Model):

    #on_delateはいちよPROTECTにしておく。ビッグデータは財産として残したいがプライバシーポリシーとも相談になる。
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='planOptimizationBenefit_companyCode',null=True, blank=True)

    vendorSelectJan = models.DecimalField(verbose_name='vendorSelectJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectFeb = models.DecimalField(verbose_name='vendorSelectFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectMar = models.DecimalField(verbose_name='vendorSelectMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectApr = models.DecimalField(verbose_name='vendorSelectApr', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectMay = models.DecimalField(verbose_name='vendorSelectMar', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectJun = models.DecimalField(verbose_name='vendorSelectJun', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectJul = models.DecimalField(verbose_name='vendorSelectJul', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectAug = models.DecimalField(verbose_name='vendorSelectAug', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectSep = models.DecimalField(verbose_name='vendorSelectSep', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectOct = models.DecimalField(verbose_name='vendorSelectOct', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectNov = models.DecimalField(verbose_name='vendorSelectNov', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    vendorSelectDec = models.DecimalField(verbose_name='vendorSelectDec', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    createdDay = models.DateTimeField(verbose_name='createdDay',null=True,blank=True,default=timezone.now)
    """記入した日付を記入してくれる"""
    updateDay = models.DateTimeField(verbose_name='updatedDay',auto_now_add=True) 


    class Meta:
        verbose_name = 'vendor Selection Benefit'
        verbose_name_plural = 'vendor Selection Benefit'
        ordering = ('-createdDay',)

    def __str__(self):
        return f"{self.companyCode}"
