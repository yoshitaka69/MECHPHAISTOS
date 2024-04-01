from django.db.models.signals import post_save
from django.dispatch import receiver
from repairingCost.models import ActualPM02, ActualPM03, ActualPM04, ActualPM05
from .models import SummedCost


@receiver(post_save, sender=ActualPM02)
@receiver(post_save, sender=ActualPM03)
@receiver(post_save, sender=ActualPM04)
@receiver(post_save, sender=ActualPM05)
def update_summed_cost_company_code(sender, instance, **kwargs):
    # SummedCost インスタンスを取得または作成
    summed_cost, created = SummedCost.objects.get_or_create(
        companyCode=instance.companyCode, 
        plant=instance.plant, 
        year=instance.year,
        defaults={'companyCode': instance.companyCode}
    )
    # companyCode を更新
    summed_cost.companyCode = instance.companyCode
    summed_cost.save()
