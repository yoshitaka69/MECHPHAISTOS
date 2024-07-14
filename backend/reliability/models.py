from django.db import models
from accounts.models import CompanyCode
from ceList.models import Equipment,Machine,CeList
from django.utils import timezone





# 故障履歴モデル
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



# 故障データモデル
class FailureData(models.Model):
    # データが保存された日時
    timestamp = models.DateTimeField(auto_now_add=True)
    # 故障までの周期（単位: 日）
    interval = models.IntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.interval}"


# ワイブル分布のデータモデル
class WeibullData(models.Model):
    failure_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)



class BayesianPrediction(models.Model):
    time = models.IntegerField()
    failure_count = models.IntegerField()
    failure_type = models.CharField(max_length=100)
    failure_cause = models.CharField(max_length=100)
    maintenance_type = models.CharField(max_length=100)
    maintenance_result = models.CharField(max_length=100)




