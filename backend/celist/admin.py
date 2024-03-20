from django.contrib import admin
from .models import CeList,Equipment,Machine


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
    list_display = ('companyCode', 'companyName','plant','ceList_Id','equipment','machineName',)
    search_fields = ('companyCode', 'companyName','plant','ceList_Id','equipment','machineName',)
    list_filter = ('companyCode', 'companyName','plant','ceList_Id','equipment','machineName',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
   
    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


# 以下でadminサイトに表示させる
admin.site.register(CeList,CeListAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Machine,MachineAdmin)
