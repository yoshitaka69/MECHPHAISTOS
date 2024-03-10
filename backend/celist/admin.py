from django.contrib import admin
from .models import CeList,Plant,Equipment,Function


class CeListAdmin(admin.ModelAdmin):
    list_display = ('companyCode','plant', 'equipment','function',)
    search_fields = ('plant', 'equipment','function',)
    list_filter = ('plant', 'equipment','function',) # adminで右側にあるフィルターBOXのこと
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

class FunctionAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','function',)
    search_fields = ('companyCode','companyName','function',)
    list_filter = ('companyCode','companyName','function',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 


# 以下でadminサイトに表示させる
admin.site.register(CeList,CeListAdmin)
admin.site.register(Plant,PlantAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Function,FunctionAdmin)

