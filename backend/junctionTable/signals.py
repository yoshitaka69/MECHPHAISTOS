from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from accounts.models import CompanyCode, Plant
from taskList.models import TaskListPPM02, TaskListPPM03, TaskListPPM05
from .models import EventYearPPM

@receiver(post_save, sender=TaskListPPM02)
@receiver(post_save, sender=TaskListPPM03)
@receiver(post_save, sender=TaskListPPM05)
def update_event_year_ppm(sender, instance, **kwargs):
    print(f"{instance._meta.model_name} {instance.taskCode} に基づいて EventYearPPM のコストを更新中")

    # CompanyCode と Plant インスタンスを取得または作成
    company_code_instance, _ = CompanyCode.objects.get_or_create(companyCode=instance.companyCode.companyCode)
    plant_instance, _ = Plant.objects.get_or_create(plant=instance.plant.plant)

    all_ppm_entries = EventYearPPM.objects.filter(companyCode=company_code_instance, plant=plant_instance)
    if not all_ppm_entries.exists():
        print(f"対応する EventYearPPM エントリが見つかりません。 companyCode: {company_code_instance.companyCode}, Plant: {plant_instance.plant}")
        new_ppm = EventYearPPM(companyCode=company_code_instance, plant=plant_instance)
        new_ppm.save()
        all_ppm_entries = [new_ppm]

    update_ppm_costs(all_ppm_entries)

def update_ppm_costs(all_ppm_entries):
    for ppm_entry in all_ppm_entries:
        for year_offset in range(11):  # 0年から10年後まで
            cost_field_name = f'PPM{year_offset}YearCost'
            labor_cost_sum = 0
            for model in [TaskListPPM02, TaskListPPM03, TaskListPPM05]:
                labor_cost_field_name = f'laborCostOfPPM{model.__name__[-2:]}'
                filter_kwargs = {
                    f'thisYear{"" if year_offset == 0 else str(year_offset) + "later"}': True,
                    "companyCode": ppm_entry.companyCode,
                    "plant": ppm_entry.plant
                }
                labor_cost_sum += model.objects.filter(**filter_kwargs).aggregate(total=Sum(labor_cost_field_name))['total'] or 0

            setattr(ppm_entry, cost_field_name, labor_cost_sum)
            print(f"{cost_field_name} を {labor_cost_sum} に設定（{ppm_entry}）")
        ppm_entry.save()
        print("EventYearPPM エントリを保存しました。")
