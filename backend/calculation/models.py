from django.db import models
from accounts.models import CompanyCode,CompanyName,Plant
from repairingCost.models import ActualPM02,ActualPM03,ActualPM04,ActualPM05


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

#summedCostのtotalCostメソッド
@receiver(post_save, sender=ActualPM02)
@receiver(post_save, sender=ActualPM03)
@receiver(post_save, sender=ActualPM04)
@receiver(post_save, sender=ActualPM05)
def update_summed_cost(sender, instance, **kwargs):
    # companyCode, plant, year は ActualPMxx モデルに適切に定義されていると仮定
    summed_cost, created = SummedCost.objects.get_or_create(
        companyCode=instance.companyCode,
        plant=instance.plant,
        year=instance.year
    )
    summed_cost.calculate_and_save_totals()


def on_actual_pm_save(sender, instance, **kwargs):
    SummedCost.update_or_create_summed_cost(
        company_code=instance.companyCode,
        plant=instance.plant,
        year=instance.year
    )

def on_actual_pm_save(sender, instance, **kwargs):
    # SummedCost インスタンスを更新または作成
    summed_cost, created = SummedCost.objects.get_or_create(
        companyCode=instance.companyCode,
        plant=instance.plant,
        year=instance.year
    )
    
    # calculate_total_for_model メソッドを呼び出して各 ActualPM モデルの合計を計算
    total_cost = SummedCost.calculate_total_for_model(sender, instance.companyCode, instance.plant, instance.year)
    
    # 適切なフィールドに合計値を設定（例: totalActualPM02）
    # sender に基づいて適切なフィールド名を決定
    field_name = f"totalActual{sender.__name__}"
    setattr(summed_cost, field_name, total_cost)
    
    # SummedCost インスタンスを保存
    summed_cost.save()
