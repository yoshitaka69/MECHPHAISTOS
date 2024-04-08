from django.contrib import admin
from .models import MasterDataTable

class MasterDataTableAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','equipment','machineName','taskPM02','taskPM03','taskPM04','taskPM05','multiTask','bomCode','bomCost','maxPartsDeliveryTimeInBom','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription')
    search_fields = ('companyCode','companyName','plant','equipment','machineName','taskPM02','taskPM03','taskPM04','taskPM05','multiTask','bomCode','bomCost','maxPartsDeliveryTimeInBom','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription')
    list_filter = ('companyCode','companyName','plant','equipment','machineName','taskPM02','taskPM03','taskPM04','taskPM05','multiTask','bomCode','bomCost','maxPartsDeliveryTimeInBom','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


# 以下でadminサイトに表示させる
admin.site.register(MasterDataTable,MasterDataTableAdmin)


class BomAndTask(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','bomCode','taskCode','bomAndTaskSet','bomAndTaskSetCost',)
    search_fields = ('companyCode','companyName','plant','bomCode','taskCode','bomAndTaskSet','bomAndTaskSetCost',)
    list_filter = ('companyCode','companyName','plant','bomCode','taskCode','bomAndTaskSet','bomAndTaskSetCost',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class AlertSchedule(admin.ModelAdmin):

    list_display = ('companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate')
    search_fields = ('companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate')
    list_filter = ('companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate'')# adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定
