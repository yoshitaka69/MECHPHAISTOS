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