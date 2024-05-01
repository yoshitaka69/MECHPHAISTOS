from django.contrib import admin
from .models import AlertSchedule



class AlertScheduleAdmin(admin.ModelAdmin):

    readonly_fields = ('orderAlertDate',)

    list_display = ('companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate', 'country')
    search_fields = ('companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate', 'country')
    list_filter = ('companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate', 'country')# adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


admin.site.register(AlertSchedule,AlertScheduleAdmin)