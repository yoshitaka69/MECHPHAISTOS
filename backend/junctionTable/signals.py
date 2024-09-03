from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from accounts.models import CompanyCode, Plant
from taskList.models import TaskListPPM02, TaskListPPM03, TaskListPPM05
from .models import EventYearPPM

from django.utils.timezone import now
from .models import GapOfRepairingCost, EventYearPPM
from calculation.models import SummedActualCost

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





# Gap計算用シグナル
@receiver(post_save, sender=EventYearPPM)
@receiver(post_save, sender=SummedActualCost)
def update_gap_cost(sender, instance, **kwargs):
    current_year = now().year

    # companyCodeを取得
    if hasattr(instance, 'companyCode') and instance.companyCode:
        company_code = instance.companyCode
    else:
        print("デバッグ: companyCodeが取得できません。")
        return

    # EventYearPPM と GapOfRepairingCost に対する処理を行う
    try:
        for i in range(-10, 11):  # 10年前から10年後まで
            year_diff = i
            target_year = current_year + i
            ppm_cost_attr = f'PPM{abs(year_diff)}YearCost' + ('Ago' if year_diff < 0 else '')
            gap_cost_attr = f'GapCostPPM{abs(year_diff)}' + ('Ago' if year_diff < 0 else '')

            # EventYearPPM からコストデータを取得
            ppm_data = EventYearPPM.objects.filter(companyCode=company_code).first()
            ppm_cost = getattr(ppm_data, ppm_cost_attr, 0) if ppm_data else 0

            # SummedActualCost から同じ年のデータを取得し合算
            actual_cost_data = SummedActualCost.objects.filter(companyCode=company_code, year=target_year)
            total_actual_cost = actual_cost_data.aggregate(total=Sum('totalActualCost'))['total'] or 0


            # 計算結果
            result = ppm_cost - total_actual_cost

            # GapOfRepairingCost にデータを保存
            gap_instance, created = GapOfRepairingCost.objects.get_or_create(companyCode=company_code)
            setattr(gap_instance, gap_cost_attr, result)
            gap_instance.save()

            print(f"デバッグ: {target_year}年 - 属性 {ppm_cost_attr} = {ppm_cost}, totalActualCost = {total_actual_cost}, 保存先属性 {gap_cost_attr} に値 {result} を保存しました。companyCode={company_code}")

    except Exception as e:
        print(f"デバッグ: 処理中にエラーが発生しました。{e}")