from django.db import models

class CeList(models.Model):

    plant = models.CharField(verbose_name='プラント名', max_length=200)
    equipment = models.CharField(verbose_name='設備名称', max_length=200)
    function = models.CharField(verbose_name='機能場所', max_length=200)
    setting_value_impact = models.CharField(verbose_name='impactへの設定値', max_length=200)
    construction_period = models.CharField(verbose_name='工期', max_length=200)
    parts_deliver_date = models.CharField(verbose_name='部品納期', max_length=200)
    mttr = models.CharField(verbose_name='MTTR', max_length=200)

    number_pm02 = models.CharField(verbose_name='PM02回数', max_length=200)
    latest_pm02 = models.CharField(verbose_name='直近のPM02', max_length=200)
    number_pm03 = models.CharField(verbose_name='PM03回数', max_length=200)
    latest_pm03 = models.CharField(verbose_name='直剣のPM03', max_length=200)
    number_pm04 = models.CharField(verbose_name='PM04回数', max_length=200)
    latest_pm04 = models.CharField(verbose_name='直近のPM04', max_length=200)

    impact_production = models.CharField(verbose_name='生産へのimpact', max_length=200)
    possibility_of_failure = models.CharField(verbose_name='故障の可能性', max_length=200)
    assessment = models.CharField(verbose_name='評価', max_length=200)

    task_pm02 = models.CharField(verbose_name='PM02タスク名称', max_length=200)
    cost_of_task = models.CharField(verbose_name='推定コスト', max_length=200)
    period_of_task = models.CharField(verbose_name='周期', max_length=200)
    next_event = models.CharField(verbose_name='次回の発生日', max_length=200)
    situation_for_pm02 = models.CharField(verbose_name='周期超過の有無', max_length=200)


class Meta:
    verbose_name_plural = 'Critical Equipment'

    def __str__(self):
     return self.plant


