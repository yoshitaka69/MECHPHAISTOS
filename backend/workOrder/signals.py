from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WorkOrder, ScheduleForCalendar

@receiver(post_save, sender=WorkOrder)
def create_or_update_schedule_for_calendar(sender, instance, created, **kwargs):
    # WorkOrderが保存されたときにScheduleForCalendarを作成または更新
    schedule, created = ScheduleForCalendar.objects.update_or_create(
        eventDataNo=instance.id,  # WorkOrderのIDを参照
        defaults={
            'companyCode': instance.companyCode,  # companyCodeを同期
            'title': instance.title,  # WorkOrderのタイトルを使用
            'startDatetime': instance.failureDate,  # failureDateを開始日として使用
            'endDatetime': instance.failureDate,  # 同じく終了日として使用
            'eventType': 'work order',  # イベントタイプを'work order'に設定
        }
    )

    # シグナルが発動したことを確認するためにターミナルにログを表示
    if created:
        print(f"ScheduleForCalendar (ID: {schedule.id}) が新規作成されました。")
    else:
        print(f"ScheduleForCalendar (ID: {schedule.id}) が更新されました。")
