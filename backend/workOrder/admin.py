from django.contrib import admin
from .models import WorkOrder, WorkPermission, WorkOrderManagement

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('workOrderNo', 'companyCode', 'plant', 'equipment', 'status', 'title', 'failureDate')
    search_fields = ('workOrderNo', 'companyCode__companyCode', 'plant__name', 'equipment', 'status', 'title')
    list_filter = ('companyCode', 'plant', 'status', 'failureDate')
    ordering = ('companyCode', 'workOrderNo')
    readonly_fields = ('workOrderNo',)



class WorkPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'workOrderNo', 'companyCode', 'companyName', 'plant', 'equipment', 'taskName', 
        'constructionPeriod', 'personInCharge', 'contractor', 'status', 'gasDetection', 
        'oxygenDeficiency', 'valve1', 'valve2', 'valve3', 'valve4', 'valve5', 
        'breaker1', 'breaker2', 'breaker3', 'breaker4', 'breaker5', 
        'onSiteSafety', 'approver', 'createdAt', 'updatedAt'
    )
    search_fields = (
        'workOrderNo__workOrderNo', 'companyCode__companyCode', 'companyName__companyName', 
        'plant__plant', 'equipment', 'taskName', 'personInCharge', 'contractor', 'status', 
        'approver'
    )
    list_filter = ('status', 'plant', 'equipment', 'gasDetection', 'oxygenDeficiency', 'onSiteSafety')
    ordering = ('workOrderNo', 'createdAt')
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class WorkOrderManagementAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', )
    search_fields = ('companyCode','companyName','plant', 'equipment',)
    list_filter = ('companyCode','companyName','plant', 'equipment',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



admin.site.register(WorkOrder,WorkOrderAdmin)
admin.site.register(WorkPermission,WorkPermissionAdmin)
admin.site.register(WorkOrderManagement,WorkOrderManagementAdmin)
