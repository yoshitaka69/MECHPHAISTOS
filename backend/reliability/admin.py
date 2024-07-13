from django.contrib import admin
from .models import TroubleHistory


class TroubleHistoryAdmin(admin.ModelAdmin):

    list_display = ('companyCode','equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'rootCause',)
    search_fields = ('companyCode','equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'rootCause',)
    list_filter = ('companyCode','equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'rootCause',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


admin.site.register(TroubleHistory,TroubleHistoryAdmin)