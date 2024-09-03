from django.contrib import admin
from .models import CeList,Equipment,Machine,RiskMatrixPossibility,RiskMatrixImpact


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','equipment')
    search_fields = ('companyCode','companyName','plant','equipment')
    list_filter = ('companyCode','companyName','plant','equipment') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
   
    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class MachineAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName','machineName')
    search_fields = ('companyCode', 'companyName','machineName')
    list_filter = ('companyCode', 'companyName','machineName') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
   
    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class CeListAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName','plant','ceListNo','equipment','machineName',)
    search_fields = ('companyCode', 'companyName','plant','ceListNo','equipment','machineName',)
    list_filter = ('companyCode', 'companyName','plant','ceListNo','equipment','machineName',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
   
    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class RiskMatrixPossibilityAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'x', 'y', 'timestamp')
    list_filter = ('companyCode', 'companyName', 'timestamp')
    search_fields = ('companyCode__code', 'companyName__name')  # Assuming `code` and `name` are fields in the related models
    ordering = ('-timestamp',)

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class RiskMatrixImpactAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'levelSetValue', 'x', 'y', 'timestamp')
    search_fields = ('companyCode__companyCode', 'companyName__companyName', 'levelSetValue')
    list_filter = ('levelSetValue', 'timestamp')



# 以下でadminサイトに表示させる
admin.site.register(CeList,CeListAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Machine,MachineAdmin)
admin.site.register(RiskMatrixPossibility,RiskMatrixPossibilityAdmin)
admin.site.register(RiskMatrixImpact,RiskMatrixImpactAdmin)