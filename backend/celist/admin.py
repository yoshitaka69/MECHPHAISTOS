from django.contrib import admin
from .models import CeList,Plant,Equipment,Machine


class CeListAdmin(admin.ModelAdmin):
    list_display = ('companyCode','plant', 'equipment','machineName','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment')
    search_fields = ('plant', 'equipment','machineName','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment')
    list_filter = ('plant', 'equipment','machineName','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
   

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

class PlantAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant',)
    search_fields = ('companyCode','companyName','plant', )
    list_filter = ('companyCode','companyName','plant',)
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','equipment',)
    search_fields = ('companyCode','companyName','equipment',)
    list_filter = ('companyCode','companyName','equipment',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 

class MachineAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','machineName','spareMachineLocationNo',)
    search_fields = ('companyCode','companyName','machineName','spareMachineLocationNo',)
    list_filter = ('companyCode','companyName','machineName','spareMachineLocationNo',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 


# 以下でadminサイトに表示させる
admin.site.register(CeList,CeListAdmin)
admin.site.register(Plant,PlantAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Machine,MachineAdmin)

