from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from repairingCost.models import ActualPM02,ActualPM03,ActualPM04,ActualPM05

#このモデルはsignal.pyを設定しているから注意
#項目が多くなるが、将来的にいろいろな企業が参加してくることを考慮し、ここは細かく設定するぞ！
class CalTablePlannedPM02(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlannedPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlannedPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTablePlannedPM02_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePlannedPM02'
        
    def __str__(self):
        return str('CalTablePlannedPM02')




class CalTableActualPM02(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM02_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM02_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM02_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    class Meta:
        verbose_name_plural = 'CalTableActualPM02'
    def __str__(self):
        return str('CalTableActualPM02')



class CalTablePlannedPM03(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlannedPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlannedPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTablePlannedPM03_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePlannedPM03'
    def __str__(self):
        return str('CalTablePlannedPM03')


class CalTableActualPM03(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM03_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM03_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM03_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
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
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTableActualPM04'
    def __str__(self):
        return str('CalTableActualPM04')



class CalTablePlannedPM05(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTablePlannedPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTablePlannedPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTablePlanPM05_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTablePlannedPM05'
    def __str__(self):
        return str('CalTablePlannedPM05')



class CalTableActualPM05(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='calTableActualPM05_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='calTableActualPM05_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE,related_name='calTableActualPM05_plant', null=True, blank=True)
    
    no1HighCost = models.DecimalField(verbose_name='no1HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1HighCostTask = models.CharField(verbose_name='no1HighCostTask', max_length=100, blank=True,null=True,)
    no2HighCost = models.DecimalField(verbose_name='no2HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no2HighCostTask = models.CharField(verbose_name='no2HighCostTask', max_length=100, blank=True,null=True,)
    no3HighCost = models.DecimalField(verbose_name='no3HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no3HighCostTask = models.CharField(verbose_name='no3HighCostTask', max_length=100, blank=True,null=True,)
    no4HighCost = models.DecimalField(verbose_name='no4HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no4HighCostTask = models.CharField(verbose_name='no4HighCostTask', max_length=100, blank=True,null=True,)
    no5HighCost = models.DecimalField(verbose_name='no5HighCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no5HighCostTask = models.CharField(verbose_name='no5HighCostTask', max_length=100, blank=True,null=True,)
    no1LowCost = models.DecimalField(verbose_name='no1LowCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    no1LowCostTask = models.CharField(verbose_name='no1LowCostTask', max_length=100, blank=True,null=True,)
    averageCost = models.DecimalField(verbose_name='averageCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'CalTableActualPM05'
    def __str__(self):
        return str('CalTableActualPM05')






class SummedPlannedCost(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='summedPlannedCost_companyCode')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='summedPlannedCost_plant')

    # 各月の合計値
    year = models.IntegerField(verbose_name='year', default=0, null=True, blank=True)
    sumJan = models.DecimalField(verbose_name='sumJan', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumFeb = models.DecimalField(verbose_name='sumFeb', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    sumMar = models.DecimalField(verbose_name='sumMay', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
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

    totalPlannedPM02 = models.DecimalField(verbose_name='totalPlannedPM02', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalPlannedPM03 = models.DecimalField(verbose_name='totalPlannedPM03', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalPlannedPM04 = models.DecimalField(verbose_name='totalPlannedPM04', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    totalPlannedPM05 = models.DecimalField(verbose_name='totalPlannedPM05', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
  
    totalPlannedCost = models.DecimalField(verbose_name='totalPlannedCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Total Planned Cost'
        ordering = ('plant',)
        
    def __str__(self):
        return f'{self.companyCode} {self.plant} {self.year}'
    
    def save(self, *args, **kwargs): #check ok 
        # 合計値を計算（None 値を考慮）
        self.totalPlannedCost = (
            (self.sumJan or 0) + (self.sumFeb or 0) + (self.sumMar or 0) + 
            (self.sumApr or 0) + (self.sumMay or 0) + (self.sumJun or 0) + 
            (self.sumJul or 0) + (self.sumAug or 0) + (self.sumSep or 0) + 
            (self.sumOct or 0) + (self.sumNov or 0) + (self.sumDec or 0) + 
            (self.sumCommitment or 0)
        )
        print(f'Calculated Total Planned Cost: {self.totalPlannedCost}')  # デバッグ情報
        super().save(*args, **kwargs)  # 親クラスのsaveメソッドを呼び出し




class SummedActualCost(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='summedActualCost_companyCode')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='summedActualCost_plant')

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
    
    def save(self, *args, **kwargs): #check ok 
        # 合計値を計算
        self.totalActualCost = (
            (self.sumJan or 0) + (self.sumFeb or 0) + (self.sumMar or 0) + 
            (self.sumApr or 0) + (self.sumMay or 0) + (self.sumJun or 0) + 
            (self.sumJul or 0) + (self.sumAug or 0) + (self.sumSep or 0) + 
            (self.sumOct or 0) + (self.sumNov or 0) + (self.sumDec or 0) + 
            (self.sumCommitment or 0)
        )
        print(f'Calculated Total Actual Cost: {self.totalActualCost}')  # デバッグ情報
        super().save(*args, **kwargs)  # 親クラスのsaveメソッドを呼び出し
