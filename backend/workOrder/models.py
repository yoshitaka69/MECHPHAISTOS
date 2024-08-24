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
    title = models.CharField(max_length=255, null=True, blank=True)  # タイトルを追加
    failureTypes = models.JSONField(null=True, blank=True)  # failureTypesはリストとして保存
    failureModes = models.JSONField(null=True, blank=True)  # failureModesもリストとして保存
    failureDescription = models.TextField(null=True, blank=True)
    failureDate = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    registrationDate = models.DateField(default=timezone.now)  # デフォルト値を現在の日付に設定

    class Meta:
        verbose_name_plural = 'Work Orders'
        ordering = ('companyCode',)
        unique_together = ('companyCode', 'workOrderNo')

    def save(self, *args, **kwargs):
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



class WorkPermission(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='workPermission_companyCode', null=True, blank=True)
    companyName = models.ForeignKey(CompanyName, on_delete=models.CASCADE, related_name='workPermission_companyName', null=True, blank=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='workPermission_plant', null=True, blank=True)
    equipment = models.CharField(max_length=100, null=True, blank=True)
    workOrderNo = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='workPermission_workOrder', null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    
    # 新しく追加するフィールド
    taskName = models.CharField(max_length=255, null=True, blank=True)
    constructionPeriod = models.CharField(max_length=100, null=True, blank=True)  # 必要に応じてDateFieldやDateRangeFieldに変更可能
    personInCharge = models.CharField(max_length=255, null=True, blank=True)  # 必要に応じてForeignKeyに変更可能

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
