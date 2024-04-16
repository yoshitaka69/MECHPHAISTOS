from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TaskListPPM02
from other_app.models import EventYearPPM  # other_app は EventYearPPM モデルがあるアプリの名前を指定してください

@receiver(post_save, sender=TaskListPPM02)
def update_event_year_ppm(sender, instance, **kwargs):
    print(f"Updating EventYearPPM costs based on TaskListPPM02 {instance.taskCode}")
    update_ppm_costs(instance)

def update_ppm_costs(task_instance):
    # EventYearPPM モデルインスタンスを取得
    all_ppm_entries = EventYearPPM.objects.filter(
        companyCode=task_instance.companyCode,
        plant=task_instance.plant
    )
    
    # TaskListPPM02 モデルから必要なデータを抽出し、整理
    for ppm_entry in all_ppm_entries:
        # 各年ごとに Boolean フィールドに基づく合計コストを計算
        for year_offset in range(11):  # 0年後から10年後まで
            field_name = f'thisYear{"" if year_offset == 0 else str(year_offset) + "later"}'
            labor_cost_sum = TaskListPPM02.objects.filter(
                **{field_name: True},
                companyCode=ppm_entry.companyCode,
                plant=ppm_entry.plant
            ).aggregate(total=Sum('laborCostOfPPM02'))['total'] or 0

            # 対応する年のコストフィールドに合計値を設定
            cost_field_name = f'PPM{year_offset}LaterCost'
            setattr(ppm_entry, cost_field_name, labor_cost_sum)
            print(f"Set {cost_field_name} to {labor_cost_sum} for {ppm_entry}")

        ppm_entry.save()
        print("Saved updated EventYearPPM entry.")

