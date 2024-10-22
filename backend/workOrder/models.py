from django.db import models
from accounts.models import CompanyCode, CompanyName,Plant








#----------------------------------------------------------------------------------------------------------------------------



from django.db import models
from django.utils import timezone
from junctionTable.models import ScheduleForCalendar

class WorkOrder(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workOrder_companyCode', null=True, blank=True)
    plant = models.CharField(max_length=100, null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)

    workOrderNo = models.CharField(max_length=100, null=True, blank=True)
    workOrderDesc = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    failureTypes = models.JSONField(null=True, blank=True)
    failureModes = models.JSONField(null=True, blank=True)
    failureCauses = models.JSONField(null=True, blank=True)  # 新しく追加
    failureDescription = models.TextField(null=True, blank=True)
    failureDate = models.DateField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    
    # 新しく追加されたフィールド
    requestType = models.CharField(max_length=100, null=True, blank=True)  # 要求タイプ
    requestedBy = models.CharField(max_length=100, null=True, blank=True)  # 要求者
    situations = models.JSONField(null=True, blank=True)  # 状況
    isUrgent = models.BooleanField(default=False)  # 緊急フラグ
    pmTypes = models.JSONField(null=True, blank=True)  # PMタイプ
    workingStartDate = models.DateField(null=True, blank=True)  # 作業開始日
    workingEndDate = models.DateField(null=True, blank=True)  # 作業終了日
    workingBy = models.CharField(max_length=100, null=True, blank=True)  # 作業者

    picture1 = models.TextField(null=True, blank=True)  # 画像1
    picture2 = models.TextField(null=True, blank=True)  # 画像2

    registrationDate = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Work Orders'
        ordering = ('companyCode',)
        unique_together = ('companyCode', 'workOrderNo')

    def save(self, *args, **kwargs):
        # workOrderNoが未設定の場合、連番を生成する
        if not self.workOrderNo:
            existing_work_order_nos = WorkOrder.objects.filter(companyCode=self.companyCode).values_list('workOrderNo', flat=True).order_by('workOrderNo')
            for i in range(1, len(existing_work_order_nos) + 2):
                candidate = str(i).zfill(5)  # 連番を生成
                if candidate not in existing_work_order_nos:
                    self.workOrderNo = candidate
                    break

        # まず、WorkOrderインスタンスを保存する
        # WorkOrderインスタンスを保存
        super(WorkOrder, self).save(*args, **kwargs)

        # ScheduleForCalendarのデータを作成/更新する際に、failureDateをタイムゾーン付きに変換
        aware_failure_date = timezone.make_aware(timezone.datetime.combine(self.failureDate, timezone.datetime.min.time()))

        # ScheduleForCalendarのエントリを作成または更新
        ScheduleForCalendar.objects.update_or_create(
            eventDataNo=self.id,
            defaults={
                'companyCode': self.companyCode,
                'title': self.title,
                'startDatetime': aware_failure_date,  # awareなdatetimeを使用
                'endDatetime': aware_failure_date,  # awareなdatetimeを使用
                'eventType': 'work order'
            }
        )

    def __str__(self):
        return f'Work Order {self.workOrderNo}'


    

#----------------------------------------------------------------------------------------------------------------------------



from django.utils import timezone
from django.db import models

class WorkPermission(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workPermission_companyCode', null=True, blank=True)
    plant = models.CharField(max_length=100, null=True, blank=True)  # Changed to CharField
    equipment = models.CharField(max_length=100, null=True, blank=True)

    workOrderNo = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='workPermission_workOrder', null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    
    # Additional fields
    taskName = models.CharField(max_length=255, null=True, blank=True)
    constructionPeriod = models.CharField(max_length=100, null=True, blank=True)
    personInCharge = models.CharField(max_length=255, null=True, blank=True)

    contractor = models.CharField(max_length=100, null=True, blank=True)
    gasDetection = models.BooleanField(default=False)
    oxygenDeficiency = models.BooleanField(default=False)

    # Storing valve and breaker input and approval separately as JSON fields
    valveInputs = models.JSONField(null=True, blank=True, default=dict)  # For valve 1-5 input states
    valveApprovals = models.JSONField(null=True, blank=True, default=dict)  # For valve 1-5 approval states
    breakerInputs = models.JSONField(null=True, blank=True, default=dict)  # For breaker 1-5 input states
    breakerApprovals = models.JSONField(null=True, blank=True, default=dict)  # For breaker 1-5 approval states

    onSiteSafety = models.BooleanField(default=False)
    approver = models.CharField(max_length=100, null=True, blank=True)
    
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Work Permissions'
        ordering = ('workOrderNo',)

    def __str__(self):
        return f'Work Permission: {self.workOrderNo}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # まずは通常通り保存

        # companyCodeとplantに基づいてWorkOrderManagementを取得
        work_order_management, created = WorkOrderManagement.objects.get_or_create(
            companyCode=self.companyCode,
            plant=self.plant
        )
        # 承認率を更新
        work_order_management.update_approval_rates()

#----------------------------------------------------------------------------------------------------------------------------


from django.utils import timezone
from django.db import models

class WorkOrderManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workOrderManagement_companyCode', null=True, blank=True)
    plant = models.CharField(max_length=100, null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)
    
    # Approval percentages for valves and breakers
    valve1_approval_rate = models.FloatField(default=0.0)
    valve2_approval_rate = models.FloatField(default=0.0)
    valve3_approval_rate = models.FloatField(default=0.0)
    valve4_approval_rate = models.FloatField(default=0.0)
    valve5_approval_rate = models.FloatField(default=0.0)
    breaker1_approval_rate = models.FloatField(default=0.0)
    breaker2_approval_rate = models.FloatField(default=0.0)
    breaker3_approval_rate = models.FloatField(default=0.0)
    breaker4_approval_rate = models.FloatField(default=0.0)
    breaker5_approval_rate = models.FloatField(default=0.0)

    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Work Order Management'
        ordering = ('companyCode',)

    def __str__(self):
        return f"Work Order Management for {self.companyCode} (Last Updated: {self.last_updated})"

    def update_approval_rates(self):
        # 指定された companyCode と plant に基づいて、WorkPermission の全件数を取得
        total_permissions = WorkPermission.objects.filter(companyCode=self.companyCode, plant=self.plant).count()

        # total_permissions が 0 より大きい場合、承認率を計算
        if total_permissions > 0:
            # 各バルブ (valve1～valve5) の承認件数を集計し、承認率を計算
            self.valve1_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, valveApprovals__valve1=True).count() / total_permissions * 100
            self.valve2_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, valveApprovals__valve2=True).count() / total_permissions * 100
            self.valve3_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, valveApprovals__valve3=True).count() / total_permissions * 100
            self.valve4_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, valveApprovals__valve4=True).count() / total_permissions * 100
            self.valve5_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, valveApprovals__valve5=True).count() / total_permissions * 100

            # 各ブレーカー (breaker1～breaker5) の承認件数を集計し、承認率を計算
            self.breaker1_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, breakerApprovals__breaker1=True).count() / total_permissions * 100
            self.breaker2_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, breakerApprovals__breaker2=True).count() / total_permissions * 100
            self.breaker3_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, breakerApprovals__breaker3=True).count() / total_permissions * 100
            self.breaker4_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, breakerApprovals__breaker4=True).count() / total_permissions * 100
            self.breaker5_approval_rate = WorkPermission.objects.filter(
                companyCode=self.companyCode, plant=self.plant, breakerApprovals__breaker5=True).count() / total_permissions * 100

            # ログ出力：承認率の計算結果をターミナルに出力
            print(f"Updated approval rates for companyCode: {self.companyCode}, plant: {self.plant}")
            print(f"Valve Approval Rates: valve1={self.valve1_approval_rate:.2f}%, valve2={self.valve2_approval_rate:.2f}%, "
                f"valve3={self.valve3_approval_rate:.2f}%, valve4={self.valve4_approval_rate:.2f}%, valve5={self.valve5_approval_rate:.2f}%")
            print(f"Breaker Approval Rates: breaker1={self.breaker1_approval_rate:.2f}%, breaker2={self.breaker2_approval_rate:.2f}%, "
                f"breaker3={self.breaker3_approval_rate:.2f}%, breaker4={self.breaker4_approval_rate:.2f}%, breaker5={self.breaker5_approval_rate:.2f}%")

        else:
            # ログ出力：承認率の計算が行われなかった場合
            print(f"No work permissions found for companyCode: {self.companyCode}, plant: {self.plant}")

        # 最後に変更を保存
        self.save()



#----------------------------------------------------------------------------------------------------------------------------

from django.db import models

class DailyReport(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='dailyReport_companyCode', null=True, blank=True)
    recorder = models.CharField(max_length=100)  # 記録者
    activity = models.TextField(blank=True, null=True)  # 活動内容（空欄を許容）
    workOrder = models.CharField(max_length=100, blank=True, null=True)  # 作業指示番号
    maintenanceType = models.CharField(max_length=100, blank=True, null=True)  # 保全の種類
    maintenanceDescription = models.TextField(blank=True, null=True)  # 保全の説明
    situation = models.TextField(blank=True, null=True)  # 状況の説明
    cause = models.TextField(blank=True, null=True)  # 原因の説明
    spareParts = models.CharField(max_length=255, blank=True, null=True)  # 使ったスペアパーツ
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  # 写真
    handwrittenNotes = models.ImageField(upload_to='handwritten_notes/', blank=True, null=True)  # 手書きノートを画像として保存
    date = models.DateField()  # 日付

    def __str__(self):
        return f"{self.recorder} - {self.date}"