from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.db.models import Avg


from .models import (CalTablePlannedPM02,CalTableActualPM02,
                     CalTablePlannedPM03,CalTableActualPM03,
                     CalTableActualPM04,
                     CalTablePlannedPM05,CalTableActualPM05,
                     SummedPlannedCost,SummedActualCost)

from taskList.models import TaskListPPM02,TaskListAPM02,TaskListPPM03,TaskListAPM03,TaskListAPM04,TaskListPPM05,TaskListAPM05
from repairingCost.models import PlannedPM02,PlannedPM03,PlannedPM05,ActualPM02,ActualPM03,ActualPM04,ActualPM05

#taskListPPM02
@receiver(post_save, sender=TaskListPPM02)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTablePlannedPM02のレコードを検索、なければ作成
    cal_table, created = CalTablePlannedPM02.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfPPM02,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfPPM02,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfPPM02,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfPPM02,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfPPM02,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfPPM02,
            'no1LowCostTask' : instance.taskName,

            
        }
    )

    if created:
        print(f"新しい CalTablePlannedPM02 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTablePlannedPM02 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfPPM02 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfPPM02
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfPPM02
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfPPM02
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfPPM02
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfPPM02
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfPPM02 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfPPM02
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfPM02の平均値を計算
    average_cost = TaskListPPM02.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfPPM02'))['laborCostOfPPM02__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTablePlannedPM02のレコードを更新
    cal_table.save()
    print("CalTablePlannedPM02 のレコードが更新されました")




#TaskListAPM02
@receiver(post_save, sender=TaskListAPM02)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTableActualPM02のレコードを検索、なければ作成
    cal_table, created = CalTableActualPM02.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfAPM02,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfAPM02,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfAPM02,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfAPM02,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfAPM02,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfAPM02,
            'no1LowCostTask' : instance.taskName,           
        }
    )

    if created:
        print(f"新しい CalTableActualPM02 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTableActualPM02 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfAPM02 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfAPM02
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfAPM02
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfAPM02
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfAPM02
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfAPM02
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfAPM02 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfAPM02
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfAPM02の平均値を計算
    average_cost = TaskListAPM02.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfAPM02'))['laborCostOfAPM02__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTableActualPM02のレコードを更新
    cal_table.save()
    print("CalTableActualPM02 のレコードが更新されました")



#taskListPPM03
@receiver(post_save, sender=TaskListPPM03)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTablePlannedPM03のレコードを検索、なければ作成
    cal_table, created = CalTablePlannedPM03.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfPPM03,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfPPM03,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfPPM03,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfPPM03,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfPPM03,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfPPM03,
            'no1LowCostTask' : instance.taskName,
        }
    )

    if created:
        print(f"新しい CalTablePlannedPM03 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTablePlannedPM03 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfPPM03 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfPPM03
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfPPM03
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfPPM03
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfPPM03
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfPPM03
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfPPM03 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfPPM03
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfPM03の平均値を計算
    average_cost = TaskListPPM03.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfPPM03'))['laborCostOfPPM03__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTablePlannedPM03のレコードを更新
    cal_table.save()
    print("CalTablePlannedPM03 のレコードが更新されました")




#TaskListAPM03
@receiver(post_save, sender=TaskListAPM03)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTableActualPM03のレコードを検索、なければ作成
    cal_table, created = CalTableActualPM03.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfAPM03,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfAPM03,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfAPM03,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfAPM03,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfAPM03,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfAPM03,
            'no1LowCostTask' : instance.taskName,           
        }
    )

    if created:
        print(f"新しい CalTableActualPM03 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTableActualPM03 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfAPM03 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfAPM03
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfAPM03
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfAPM03
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfAPM03
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfAPM03
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfAPM03 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfAPM03
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfAPM03の平均値を計算
    average_cost = TaskListAPM03.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfAPM03'))['laborCostOfAPM03__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTableActualPM03のレコードを更新
    cal_table.save()
    print("CalTableActualPM03 のレコードが更新されました")



#TaskListAPM04
@receiver(post_save, sender=TaskListAPM04)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTableActualPM04のレコードを検索、なければ作成
    cal_table, created = CalTableActualPM04.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfAPM04,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfAPM04,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfAPM04,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfAPM04,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfAPM04,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfAPM04,
            'no1LowCostTask' : instance.taskName,           
        }
    )

    if created:
        print(f"新しい CalTableActualPM04 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTableActualPM04 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfAPM04 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfAPM04
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfAPM04
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfAPM04
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfAPM04
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfAPM04
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfAPM04 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfAPM04
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfAPM04の平均値を計算
    average_cost = TaskListAPM04.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfAPM04'))['laborCostOfAPM04__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTableActualPM04のレコードを更新
    cal_table.save()
    print("CalTableActualPM04 のレコードが更新されました")



#taskListPPM05
@receiver(post_save, sender=TaskListPPM05)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTablePlannedPM05のレコードを検索、なければ作成
    cal_table, created = CalTablePlannedPM05.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfPPM05,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfPPM05,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfPPM05,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfPPM05,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfPPM05,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfPPM05,
            'no1LowCostTask' : instance.taskName,
        }
    )

    if created:
        print(f"新しい CalTablePlannedPM05 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTablePlannedPM05 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfPPM05 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfPPM05
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfPPM05
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfPPM05
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfPPM05
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfPPM05
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfPPM05 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfPPM05
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfPM05の平均値を計算
    average_cost = TaskListPPM05.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfPPM05'))['laborCostOfPPM05__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTablePlannedPM05のレコードを更新
    cal_table.save()
    print("CalTablePlannedPM05 のレコードが更新されました")


#TaskListAPM05
@receiver(post_save, sender=TaskListAPM05)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTableActualPM05のレコードを検索、なければ作成
    cal_table, created = CalTableActualPM05.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfAPM05,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfAPM05,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfAPM05,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfAPM05,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfAPM05,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfAPM05,
            'no1LowCostTask' : instance.taskName,           
        }
    )

    if created:
        print(f"新しい CalTableActualPM05 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTableActualPM05 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
    if instance.laborCostOfAPM05 > cal_table.no1HighCost:
        cal_table.no1HighCost = instance.laborCostOfAPM05
        cal_table.no1HighCostTask = instance.taskName
            
    # no2HighCost, no3HighCost...等の同様のロジックを実装
        cal_table.no2HighCost = instance.laborCostOfAPM05
        cal_table.no2HighCostTask = instance.taskName

        cal_table.no3HighCost = instance.laborCostOfAPM05
        cal_table.no3HighCostTask = instance.taskName

        cal_table.no4HighCost = instance.laborCostOfAPM05
        cal_table.no4HighCostTask = instance.taskName

        cal_table.no5HighCost = instance.laborCostOfAPM05
        cal_table.no5HighCostTask = instance.taskName
        
    # 最低コストの更新
    if instance.laborCostOfAPM05 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
        cal_table.no1LowCost = instance.laborCostOfAPM05
        cal_table.no1LowCostTask = instance.taskName

    # 指定されたcompanyCodeに対するlaborCostOfAPM05の平均値を計算
    average_cost = TaskListAPM05.objects.filter(
        companyCode=instance.companyCode
    ).aggregate(Avg('laborCostOfAPM05'))['laborCostOfAPM05__avg']

    # averageCostの更新
    if average_cost is not None:
        cal_table.averageCost = average_cost

    # CalTableActualPM05のレコードを更新
    cal_table.save()
    print("CalTableActualPM05 のレコードが更新されました")










# total Planned Cost
def update_summed_planned_cost(instance):
    print(f'Updating summed planned cost for {instance}')

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment']
    totals = {f'sum{month}': 0 for month in months}

    # plannedPM02からplannedPM05までの値を取得し合計
    for pm_model in [PlannedPM02, PlannedPM03, PlannedPM05]:
        pm_records = pm_model.objects.filter(year=instance.year, companyCode=instance.companyCode, plant=instance.plant)
        print(f'Found {pm_records.count()} records in {pm_model.__name__} for year {instance.year}, companyCode {instance.companyCode}, plant {instance.plant}')

        for obj in pm_records:
            for month in months:
                field_name = month.lower()
                value = getattr(obj, field_name, 0)
                totals[f'sum{month}'] += value
                print(f'Adding {value} to sum{month} from {obj} in {pm_model.__name__}')

    # SummedPlannedCostオブジェクトの取得または作成
    spc, created = SummedPlannedCost.objects.get_or_create(
        companyCode=instance.companyCode,
        plant=instance.plant,
        year=instance.year
    )
    print(f'{"Created" if created else "Retrieved"} SummedPlannedCost instance: {spc}')

    # 合計値の更新
    for month, total in totals.items():
        setattr(spc, month, total)
        print(f'Set {month} to {total} in SummedPlannedCost')

    spc.save()
    print(f'SummedPlannedCost instance saved: {spc}')

# plannedPM02からplannedPM05が保存・更新された際に呼び出されるシグナル
@receiver(post_save, sender=PlannedPM02)
@receiver(post_save, sender=PlannedPM03)
@receiver(post_save, sender=PlannedPM05)
def planned_pm_post_save(sender, instance, **kwargs):
    print(f'post_save signal received for {sender.__name__} with instance {instance}')
    update_summed_planned_cost(instance)

# PlannedPM02からPlannedPM05が削除された際に実行
@receiver(post_delete, sender=PlannedPM02)
@receiver(post_delete, sender=PlannedPM03)
@receiver(post_delete, sender=PlannedPM05)
def planned_pm_post_delete(sender, instance, **kwargs):
    print(f'post_delete signal received for {sender.__name__} with instance {instance}')
    update_summed_planned_cost(instance)




#total Actual Cost
def update_summed_actual_cost(instance):
    print(f'Updating summed actual cost for {instance}')

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Commitment']
    totals = {f'sum{month}': 0 for month in months}

    # actualPM02とactualPM03から値を取得し合計
    for pm_model in [ActualPM02, ActualPM03,ActualPM04,ActualPM05]:
        pm_records = pm_model.objects.filter(year=instance.year, companyCode=instance.companyCode, plant=instance.plant)
        print(f'Found {pm_records.count()} records in {pm_model.__name__} for year {instance.year}, companyCode {instance.companyCode}, plant {instance.plant}')

        for obj in pm_records:
            for month in months:
                field_name = month.lower()
                value = getattr(obj, field_name, 0)
                totals[f'sum{month}'] += value
                print(f'Adding {value} to sum{month} from {obj} in {pm_model.__name__}')

    # SummedActualCostオブジェクトの取得または作成
    sac, created = SummedActualCost.objects.get_or_create(
        companyCode=instance.companyCode,
        plant=instance.plant,
        year=instance.year
    )
    print(f'{"Created" if created else "Retrieved"} SummedActualCost instance: {sac}')

    # 合計値の更新
    for month, total in totals.items():
        setattr(sac, month, total)
        print(f'Set {month} to {total} in SummedActualCost')

    sac.save()
    print(f'SummedActualCost instance saved: {sac}')

# actualPM02またはactualPM03が保存・更新された際に呼び出されるシグナル
@receiver(post_save, sender=ActualPM02)
@receiver(post_save, sender=ActualPM03)
@receiver(post_save, sender=ActualPM04)
@receiver(post_save, sender=ActualPM05)

def actual_pm_post_save(sender, instance, **kwargs):
    print(f'post_save signal received for {sender.__name__} with instance {instance}')
    update_summed_actual_cost(instance)


# ActualPM02またはActualPM03が削除された際に実行
@receiver(post_delete, sender=ActualPM02)
@receiver(post_delete, sender=ActualPM03)
@receiver(post_delete, sender=ActualPM04)
@receiver(post_delete, sender=ActualPM05)
def actual_pm_post_delete(sender, instance, **kwargs):
    print(f'post_delete signal received for {sender.__name__} with instance {instance}')
    update_summed_actual_cost(instance)