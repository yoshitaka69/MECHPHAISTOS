from django.contrib import admin
from .models import WorkOrder, WorkPermission, WorkOrderManagement

class WorkOrderAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'workOrderNo','workOrderDesc','status')
    search_fields = ('companyCode','companyName','plant', 'equipment', 'workOrderNo','workOrderDesc','status')
    list_filter = ('companyCode','companyName','plant', 'equipment', 'workOrderNo','workOrderDesc','status') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class WorkPermissionAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'workOrderNo', 'workPermissionNo', 'workPermissionDesc','status')
    search_fields = ('companyCode','companyName','plant', 'equipment', 'workOrderNo', 'workPermissionNo', 'workPermissionDesc','status')
    list_filter = ('companyCode','companyName','plant', 'equipment', 'workOrderNo', 'workPermissionNo', 'workPermissionDesc','status') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
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
