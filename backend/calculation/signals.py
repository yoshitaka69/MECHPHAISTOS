from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CalTablePlannedPM02
from taskList.models import TaskListPM02

@receiver(post_save, sender=TaskListPM02)
def update_or_create_cal_table(sender, instance, **kwargs):
    print("update_or_create_cal_table シグナルがトリガーされました")

    # CalTablePlannedPM02のレコードを検索、なければ作成
    cal_table, created = CalTablePlannedPM02.objects.get_or_create(
        companyCode=instance.companyCode,
        defaults={
            'no1HighCost': instance.laborCostOfPM02,
            'no1HighCostTask': instance.taskName,
            
            'no2HighCost': instance.laborCostOfPM02,
            'no2HighCostTask': instance.taskName,

            'no3HighCost': instance.laborCostOfPM02,
            'no3HighCostTask': instance.taskName,

            'no4HighCost': instance.laborCostOfPM02,
            'no4HighCostTask': instance.taskName,

            'no5HighCost': instance.laborCostOfPM02,
            'no5HighCostTask': instance.taskName,

            'no1LowCost' : instance.laborCostOfPM02,
            'no1LowCostTask' : instance.taskName,

            
        }
    )

    if created:
        print(f"新しい CalTablePlannedPM02 のレコードが作成されました: {cal_table}")
    else:
        print(f"既存の CalTablePlannedPM02 のレコードが見つかりました: {cal_table}")
        # レコードが既に存在する場合は、必要に応じて値を更新
        if instance.laborCostOfPM02 > cal_table.no1HighCost:
            print(f"no1HighCost を更新します: 古い値={cal_table.no1HighCost}, 新しい値={instance.laborCostOfPM02}")
            cal_table.no1HighCost = instance.laborCostOfPM02
            cal_table.no1HighCostTask = instance.taskName
            
        # no2HighCost, no3HighCost...等の同様のロジックを実装
            cal_table.no2HighCost = instance.laborCostOfPM02
            cal_table.no2HighCostTask = instance.taskName

            cal_table.no3HighCost = instance.laborCostOfPM02
            cal_table.no3HighCostTask = instance.taskName

            cal_table.no4HighCost = instance.laborCostOfPM02
            cal_table.no4HighCostTask = instance.taskName

            cal_table.no5HighCost = instance.laborCostOfPM02
            cal_table.no5HighCostTask = instance.taskName
        
        # 最低コストの更新
        if instance.laborCostOfPM02 < cal_table.no1LowCost or cal_table.no1LowCost == 0:
            print(f"no1LowCost を更新します: 古い値={cal_table.no1LowCost}, 新しい値={instance.laborCostOfPM02}")
            cal_table.no1LowCost = instance.laborCostOfPM02
            cal_table.no1LowCostTask = instance.taskName

    # CalTablePlannedPM02のレコードを更新
    cal_table.save()
    print("CalTablePlannedPM02 のレコードが更新されました")
