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
        # 管理画面で表示されるモデル名の複数形を「Work Orders」に設定
        verbose_name_plural = 'Work Orders'

        # デフォルトの並び順をcompanyCodeの順番にする
        ordering = ('companyCode',)

        # companyCodeとworkOrderNoの組み合わせが一意であることを保証する
        unique_together = ('companyCode', 'workOrderNo')

    # saveメソッドをオーバーライドして、workOrderNoが未設定の場合に自動的に番号を生成する
    def save(self, *args, **kwargs):
        if not self.workOrderNo:
            # 既存の作業指示番号を取得し、番号を自動生成するロジック
            existing_work_order_nos = WorkOrder.objects.filter(companyCode=self.companyCode).values_list('workOrderNo', flat=True).order_by('workOrderNo')
            
            # 1から順に、既存の番号をチェックしながら未使用の番号を探す
            for i in range(1, len(existing_work_order_nos) + 2):
                candidate = str(i).zfill(5)  # ゼロパディングで5桁の番号を生成
                if candidate not in existing_work_order_nos:
                    self.workOrderNo = candidate  # 使用されていない番号をworkOrderNoに設定
                    break

        # オーバーライドしたsaveメソッドで親クラスのsaveも実行
        super(WorkOrder, self).save(*args, **kwargs)

    # 作業指示を文字列として返す際の表示形式を定義
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
