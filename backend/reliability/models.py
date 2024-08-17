from django.db import models
from accounts.models import CompanyCode
from ceList.models import Equipment,Machine,CeList
from django.utils import timezone
from datetime import date



# Reliability
#-------------------------------------------------------------------------------------------------------------------------------------
class Reliability(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='reliability_companyCode', null=True, blank=True)
    ceListNo = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='reliability_ceListNo', null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='reliability_equipment', null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='reliability_machine', null=True, blank=True)

    mttr = models.IntegerField(verbose_name='MTTR', null=True, blank=True)  
    mtbf = models.IntegerField(verbose_name='MTBF', null=True, blank=True)  
    mttf = models.IntegerField(verbose_name='MTTF', null=True, blank=True)  
    totalOperatingTime = models.FloatField(verbose_name='Total Operating Time', null=True, blank=True)  # 総稼働時間
    failureCount = models.IntegerField(verbose_name='Failure Count', null=True, blank=True)  # 故障回数

    # 追加するフィールド
    failureType = models.IntegerField(
        choices=[
            (1, '機械的故障'),
            (2, '電気的故障'),
            (3, '両方')
        ],
        null=True, blank=True,
        verbose_name='Failure Type'
    )
    failureMode = models.IntegerField(
        choices=[
            (1, 'PM03'),
            (2, 'PM04')
        ],
        null=True, blank=True,
        verbose_name='Failure Mode'
    )
    maintenanceMethod = models.IntegerField(
        choices=[
            (1, '検査'),
            (2, '定期保全'),
            (3, '部品交換'),
            (4, 'オーバーホール')
        ],
        null=True, blank=True,
        verbose_name='Maintenance Method'
    )
    maintenanceFrequency = models.IntegerField(null=True, blank=True, verbose_name='Maintenance Frequency')  # メンテナンス頻度
    maintenanceImpact = models.FloatField(null=True, blank=True, verbose_name='Maintenance Impact')  # メンテナンスの影響
    failureCause = models.IntegerField(
        choices=[
            (1, '過負荷'),
            (2, '摩耗'),
            (3, '環境要因')
        ],
        null=True, blank=True,
        verbose_name='Failure Cause'
    )
    environmentCondition = models.FloatField(null=True, blank=True, verbose_name='Environmental Conditions')  # 環境条件（スケール）
    operationalCondition = models.IntegerField(
        choices=[
            (0, '通常運転'),
            (1, '過負荷'),
            (2, '過熱')
        ],
        null=True, blank=True,
        verbose_name='Operational Conditions'
    )
    componentCondition = models.FloatField(null=True, blank=True, verbose_name='Component Condition')  # 部品の摩耗度

        # 新規追加
    record_date = models.DateField(verbose_name='Record Date', default=date.today)

    class Meta:
        ordering = ['-mttr']

#-------------------------------------------------------------------------------------------------------------------------------------



# 故障履歴モデル(PrecisionAndAccuracy)
#-------------------------------------------------------------------------------------------------------------------------------------
class TroubleHistory(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='troubleHistory_companyCode', null=True, blank=True)
    ceListNo = models.ForeignKey(CeList, on_delete=models.CASCADE, related_name='troubleHistory_ceListNo',null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='troubleHistory_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='troubleHistory_machine',null=True, blank=True)

    date = models.DateField(verbose_name='date', null=True, blank=True, default=timezone.now)
    pmType = models.CharField(verbose_name='pmType', max_length=50, null=True, blank=True)
    failureContent = models.TextField(verbose_name='failureContent', max_length=1000, null=True, blank=True)
    failureType = models.CharField(verbose_name='failureType', max_length=50, null=True, blank=True)
    repairMethod = models.TextField(verbose_name='repairMethod', max_length=1000, null=True, blank=True)
    repairCost = models.DecimalField(verbose_name='repairCost', max_digits=12, decimal_places=2,default=0,null=True, blank=True)
    rootCause = models.TextField(verbose_name='rootCause', max_length=1000, null=True, blank=True)

    class Meta:
        ordering = ['-date']


#-------------------------------------------------------------------------------------------------------------------------------------



# 故障予測ポイントモデル(PrecisionAndAccuracy)
#-------------------------------------------------------------------------------------------------------------------------------------
class FailurePredictionPoint(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='failurePredictionPoint_companyCode', null=True, blank=True)
    ceListNo = models.CharField(verbose_name='ceListNo', max_length=100,blank=True,null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='failurePredictionPoint_equipment',null=True, blank=True)
    machineName = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='failurePredictionPoint_machine',null=True, blank=True)

    date = models.DateField(verbose_name='date', null=True, blank=True, default=timezone.now)
    pmType = models.CharField(verbose_name='pmType', max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['-date']


#-------------------------------------------------------------------------------------------------------------------------------------







