from django.contrib import admin
from .models import CeList,Plant


class CeListAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName','plant','ceList_Id','equipment','machineName',)
    search_fields = ('companyCode', 'companyName','plant','ceList_Id','equipment','machineName',)
    list_filter = ('companyCode', 'companyName','plant','ceList_Id','equipment','machineName',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
   
    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


# 以下でadminサイトに表示させる
admin.site.register(CeList,CeListAdmin)

