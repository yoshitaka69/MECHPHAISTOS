from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from accounts.models import CompanyCode, Plant
from taskList.models import TaskListPPM02, TaskListPPM03, TaskListPPM05
from .models import EventYearPPM

from django.utils.timezone import now
from .models import GapOfRepairingCost, EventYearPPM, SummedActualCost


@receiver(post_save, sender=TaskListPPM02)
@receiver(post_save, sender=TaskListPPM03)
@receiver(post_save, sender=TaskListPPM05)
def update_event_year_ppm(sender, instance, **kwargs):
    print(f"{instance._meta.model_name} {instance.taskCode} に基づいて EventYearPPM のコストを更新中")

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
        # 未来のコストデータの更新
        for year_offset in range(11):
            cost_field_name = f'PPM{year_offset}YearCost'
            update_ppm_year_cost(ppm_entry, year_offset, cost_field_name, future=True)

        # 過去のコストデータの更新
        for year_offset in range(1, 11):
            cost_field_name = f'PPM{year_offset}YearCostAgo'
            update_ppm_year_cost(ppm_entry, year_offset, cost_field_name, future=False)
            
        ppm_entry.save()
        print("EventYearPPM エントリを保存しました。")

def update_ppm_year_cost(ppm_entry, year_offset, cost_field_name, future=True):
    labor_cost_sum = 0
    if year_offset == 0:
        year_field = 'thisYear'  # 現在の年を表すフィールド
    else:
        year_qualifier = "later" if future else "ago"
        year_field = f'thisYear{year_offset}{year_qualifier}'
    
    for model in [TaskListPPM02, TaskListPPM03, TaskListPPM05]:
        labor_cost_field_name = f'laborCostOfPPM{model.__name__[-2:]}'
        filter_kwargs = {
            year_field: True,
            "companyCode": ppm_entry.companyCode,
            "plant": ppm_entry.plant
        }
        labor_cost_sum += model.objects.filter(**filter_kwargs).aggregate(total=Sum(labor_cost_field_name))['total'] or 0

    setattr(ppm_entry, cost_field_name, labor_cost_sum)
    print(f"{cost_field_name} を {labor_cost_sum} に設定（{ppm_entry}）")




*Gap計算用
@receiver(post_save, sender=GapOfRepairingCost)
def calculate_gap(sender, instance, **kwargs):
    current_year = now().year

    # 10年前から10年後までの範囲で処理を行う
    for i in range(-10, 11):  # -10 は 10 年前、0 は現在年、10 は 10 年後
        target_year = current_year + i
        attr_name = f'PPM{-i}YearCost' if i <= 0 else f'PPM{i}YearCostAgo'
        gap_attr_name = f'GapCostPPM{-i}Ago' if i < 0 else f'GapCostPPM{i}' if i >= 0 else 'GapCostPPM0'
        
        try:
            ppm_data = EventYearPPM.objects.get(year=target_year)
            ppm_cost = getattr(ppm_data, attr_name, 0)
        except EventYearPPM.DoesNotExist:
            print(f"{target_year}年のPPMデータが存在しません。")
            ppm_cost = 0

        # SummedActualCostから同じ年のデータを取得
        try:
            actual_cost_data = SummedActualCost.objects.get(year=target_year)
            total_actual_cost = actual_cost_data.totalActualCost
        except SummedActualCost.DoesNotExist:
            print(f"{target_year}年の実際のコストデータが存在しません。")
            total_actual_cost = 0

        # 計算結果
        result = ppm_cost - total_actual_cost

        # 結果を対応するフィールドに保存
        setattr(instance, gap_attr_name, result)

    instance.save()  # インスタンスの変更を保存

# モデルを保存するためのコード例
def save_instance():
    instance = GapOfRepairingCost()
    instance.save()
