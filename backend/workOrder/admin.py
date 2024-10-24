from django.contrib import admin
from .models import WorkOrder, WorkPermission, WorkOrderManagement

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('workOrderNo', 'companyCode', 'plant', 'equipment', 'status', 'title', 'failureDate')
    search_fields = ('workOrderNo', 'companyCode__companyCode', 'plant__name', 'equipment', 'status', 'title')
    list_filter = ('companyCode', 'plant', 'status', 'failureDate')
    ordering = ('companyCode', 'workOrderNo')
    readonly_fields = ('workOrderNo',)





class WorkPermissionAdmin(admin.ModelAdmin):
    # 管理画面で表示するフィールドを指定
    list_display = (
        'workOrderNo','workPermissionNo', 'companyCode', 'plant', 'equipment', 
        'status', 'taskName', 'personInCharge', 
        'contractor', 'gasDetection', 'oxygenDeficiency', 
        'onSiteSafety', 'approver', 'createdAt', 'updatedAt'
    )

    # 管理画面で検索可能なフィールド
    search_fields = ('workOrderNo', 'plant', 'taskName', 'personInCharge', 'contractor', 'approver')

    # フィルタリング機能を追加
    list_filter = ('plant', 'status', 'gasDetection', 'oxygenDeficiency', 'onSiteSafety')

    # 編集可能なフィールドを指定
    fieldsets = (
        (None, {
            'fields': (
                'companyCode', 'plant', 'equipment', 'workOrderNo', 'status',
                'taskName', 'constructionPeriod', 'personInCharge', 'contractor', 
                'gasDetection', 'oxygenDeficiency', 'onSiteSafety', 'approver'
            )
        }),
        ('Valve Inputs and Approvals', {
            'fields': ('valveInputs', 'valveApprovals'),
        }),
        ('Breaker Inputs and Approvals', {
            'fields': ('breakerInputs', 'breakerApprovals'),
        }),
        ('Timestamps', {
            'fields': ('createdAt', 'updatedAt'),
        }),
    )
    # 編集画面で読み取り専用のフィールド
    readonly_fields = ('createdAt', 'updatedAt')





class WorkOrderManagementAdmin(admin.ModelAdmin):
    # 管理画面で表示するフィールドのリスト
    list_display = (
        'companyCode', 'plant', 'equipment', 
        'valve1_approval_rate', 'valve2_approval_rate', 'valve3_approval_rate', 
        'valve4_approval_rate', 'valve5_approval_rate', 
        'breaker1_approval_rate', 'breaker2_approval_rate', 'breaker3_approval_rate', 
        'breaker4_approval_rate', 'breaker5_approval_rate', 'last_updated'
    )
    
    # 編集可能なフィールドのリスト
    list_editable = (
        'valve1_approval_rate', 'valve2_approval_rate', 'valve3_approval_rate', 
        'valve4_approval_rate', 'valve5_approval_rate', 
        'breaker1_approval_rate', 'breaker2_approval_rate', 'breaker3_approval_rate', 
        'breaker4_approval_rate', 'breaker5_approval_rate'
    )
    
    # フィルターオプション
    list_filter = ('companyCode', 'plant', 'last_updated')

    # 検索可能なフィールド
    search_fields = ('companyCode', 'plant', 'equipment')

    # ページング（1ページあたりの表示件数）
    list_per_page = 25




admin.site.register(WorkOrder,WorkOrderAdmin)
admin.site.register(WorkPermission,WorkPermissionAdmin)
admin.site.register(WorkOrderManagement,WorkOrderManagementAdmin)
