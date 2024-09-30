from django.db import models
from accounts.models import CompanyCode, CompanyName,Plant








#----------------------------------------------------------------------------------------------------------------------------



from django.db import models
from django.utils import timezone

class WorkOrder(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workOrder_companyCode', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workOrder_plant', null=True, blank=True)
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
        # workOrderNo が未設定の場合、自動で連番を生成
        if not self.workOrderNo:
            existing_work_order_nos = WorkOrder.objects.filter(companyCode=self.companyCode).values_list('workOrderNo', flat=True).order_by('workOrderNo')
            for i in range(1, len(existing_work_order_nos) + 2):
                candidate = str(i).zfill(5)
                if candidate not in existing_work_order_nos:
                    self.workOrderNo = candidate
                    break

        super(WorkOrder, self).save(*args, **kwargs)

    def __str__(self):
        return f'Work Order {self.workOrderNo}'


    

#----------------------------------------------------------------------------------------------------------------------------



from django.utils import timezone

class WorkPermission(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workPermission_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='workPermission_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workPermission_plant', null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)

    workOrderNo = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='workPermission_workOrder', null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    
    # 新しく追加するフィールド
    taskName = models.CharField(max_length=255, null=True, blank=True)
    constructionPeriod = models.CharField(max_length=100, null=True, blank=True)
    personInCharge = models.CharField(max_length=255, null=True, blank=True)

    # SafetyRequest のフィールドを統合
    contractor = models.CharField(max_length=100, null=True, blank=True)
    gasDetection = models.BooleanField(default=False)
    oxygenDeficiency = models.BooleanField(default=False)
    valve1 = models.BooleanField(default=False)
    valve2 = models.BooleanField(default=False)
    valve3 = models.BooleanField(default=False)
    valve4 = models.BooleanField(default=False)
    valve5 = models.BooleanField(default=False)
    breaker1 = models.BooleanField(default=False)
    breaker2 = models.BooleanField(default=False)
    breaker3 = models.BooleanField(default=False)
    breaker4 = models.BooleanField(default=False)
    breaker5 = models.BooleanField(default=False)
    onSiteSafety = models.BooleanField(default=False)
    approver = models.CharField(max_length=100, null=True, blank=True)
    
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Work Permissions'
        ordering = ('workOrderNo',)

    def __str__(self):
        return f'Work Permission: {self.workOrderNo}'



#----------------------------------------------------------------------------------------------------------------------------


class WorkOrderManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workOrderManagement_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='workOrderManagement_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workOrderManagement_plant', null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Work Order Management'
        ordering = ('companyCode',)
    def __str__(self):
        return str('Work Order Management')




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