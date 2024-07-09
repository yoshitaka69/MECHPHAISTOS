from django.db import models

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