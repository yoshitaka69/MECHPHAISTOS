from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from accounts.models import CompanyCode
from taskList.models import TaskListPPM02
from .models import EventYearPPM
from django.db.models import Sum



@receiver(post_save, sender=CompanyCode)
def update_event_year_ppm(sender, instance, created, **kwargs):
    # このシグナルは実際には CompanyCode の companyCode フィールドの更新には反応する必要がありません。
    # CompanyCode の作成のみを検知すれば十分です。
    if created:
        print(f'新規 CompanyCode が作成されました: {instance.companyCode}')

@receiver(pre_delete, sender=CompanyCode)
def delete_related_event_year_ppm(sender, instance, **kwargs):
    affected_rows = EventYearPPM.objects.filter(companyCode=instance).delete()
    print(f'削除された CompanyCode {instance.companyCode}: 関連する EventYearPPM の行数 {affected_rows[0]}')





@receiver(post_save, sender=TaskListPPM02)
def update_event_year_ppm(sender, instance, **kwargs):
    print(f"TaskListPPM02 {instance.taskCode} に基づいて EventYearPPM のコストを更新中")

    # companyCode と plant の実際のフィールドを使用して EventYearPPM をフィルタリング
    all_ppm_entries = EventYearPPM.objects.filter(
        companyCode__companyCode=instance.companyCode.companyCode,
        plant__plant=instance.plant.plant
    )
    
    if not all_ppm_entries.exists():
        print(f"対応する EventYearPPM エントリが見つかりません。 companyCode: {instance.companyCode.companyCode}, Plant: {instance.plant.plant}")
        return

    update_ppm_costs(instance, all_ppm_entries)

def update_ppm_costs(task_instance, all_ppm_entries):
    for ppm_entry in all_ppm_entries:
        for year_offset in range(11):  # 0年から10年後まで
            field_name = f'thisYear{"" if year_offset == 0 else str(year_offset) + "later"}'
            filter_kwargs = {field_name: True, "companyCode": ppm_entry.companyCode, "plant": ppm_entry.plant}
            labor_cost_sum = TaskListPPM02.objects.filter(**filter_kwargs).aggregate(total=Sum('laborCostOfPPM02'))['total'] or 0

            cost_field_name = f'PPM{year_offset}YearCost'
            setattr(ppm_entry, cost_field_name, labor_cost_sum)
            print(f"{cost_field_name} を {labor_cost_sum} に設定（{ppm_entry}）")

        ppm_entry.save()
        print("EventYearPPM エントリを保存しました。")
