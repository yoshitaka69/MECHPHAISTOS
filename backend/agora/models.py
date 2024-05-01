from django.db import models
from django.utils import timezone
from datetime import timedelta
import decimal

from accounts.models import CompanyCode,CompanyName,Plant,AreaCode
from spareParts.models import SpareParts




class AlertSchedule(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='alertSchedule_companyCode',null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='alertSchedule_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='alertSchedule_plant',null=True, blank=True)
    partsName = models.ForeignKey(SpareParts, on_delete=models.CASCADE, related_name='alertSchedule_partsName',null=True, blank=True)
    eventDate = models.DateField(verbose_name='eventDate', blank=True, null=True, default=timezone.now)
    deliveryTime = models.IntegerField(verbose_name='deliveryTime',null=True,blank=True,default=0)
    orderAlertDate = models.DateField(verbose_name='orderAlertDate',blank=True,null=True)
    safetyRate = models.CharField(verbose_name='safetyRate',blank=True,null=True,max_length=100)
    country = models.ForeignKey(AreaCode,on_delete=models.CASCADE, related_name='alertSchedule_areaCode',null=True, blank=True)

    class Meta:
        verbose_name = 'AlertSchedule'
        verbose_name_plural = 'AlertSchedule'
        ordering = ('companyCode',) #モデルのクエリセットを取得した際にどのような順番でフィールドを並べ変えるかを決める。
    

    def __str__(self):
        return str('AlertSchedule')

    #orderAlertDateを算出する関数 　 CHECK OK 
    def calculate_order_alert_date(self):
        if self.eventDate and self.deliveryTime is not None and self.safetyRate:
            try:
                # deliveryTime を timedelta に変換
                delivery_timedelta = timedelta(days=self.deliveryTime)

                # eventDate から deliveryTime を引く
                estimated_date = self.eventDate - delivery_timedelta

                # safetyRate を小数に変換（例: "50%" -> 0.5）
                safety_rate_decimal = decimal.Decimal(self.safetyRate.strip('%')) / 100

                # 差分日数から safetyRate 分を引く（修正された部分）
                additional_days = int(delivery_timedelta.days * safety_rate_decimal)

                # eventDate から引く（修正された部分）
                new_order_alert_date = estimated_date - timedelta(days=additional_days)

                # 新しい値を設定
                self.orderAlertDate = new_order_alert_date.strftime("%Y-%m-%d")
            except (ValueError, TypeError, decimal.InvalidOperation):
                # 変換エラーや型エラー、無効な操作の場合は何もしない（あるいはエラーログを出力）
                pass

    def save(self, *args, **kwargs):
        self.calculate_order_alert_date()
        super().save(*args, **kwargs)
