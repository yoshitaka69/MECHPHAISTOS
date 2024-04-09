from django.contrib import admin
from .models import MasterDataTable,BomAndTask

class MasterDataTableAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','ceListNo','equipment','machineName','taskPM02','countOfPM02','latestPM02','laborCostOfPM02','taskPM03','countOfPM03','latestPM03','laborCostOfPM03','taskPM04','countOfPM04','latestPM04','laborCostOfPM04','taskPM05','countOfPM05','latestPM05','laborCostOfPM05','typicalTaskName','typicalConstPeriod','typicalTaskCost','typicalNextEventDate','typicalSituation','multiTask','bomCode','bomCost','bomStock','maxPartsDeliveryTimeInBom','totalCost','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later')
    search_fields = ('companyCode','companyName','plant','ceListNo','equipment','machineName','taskPM02','countOfPM02','latestPM02','laborCostOfPM02','taskPM03','countOfPM03','latestPM03','laborCostOfPM03','taskPM04','countOfPM04','latestPM04','laborCostOfPM04','taskPM05','countOfPM05','latestPM05','laborCostOfPM05','typicalTaskName','typicalConstPeriod','typicalTaskCost','typicalNextEventDate','typicalSituation','multiTask','bomCode','bomCost','bomStock','maxPartsDeliveryTimeInBom','totalCost','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later')
    list_filter = ('companyCode','companyName','plant','ceListNo','equipment','machineName','taskPM02','countOfPM02','latestPM02','laborCostOfPM02','taskPM03','countOfPM03','latestPM03','laborCostOfPM03','taskPM04','countOfPM04','latestPM04','laborCostOfPM04','taskPM05','countOfPM05','latestPM05','laborCostOfPM05','typicalTaskName','typicalConstPeriod','typicalTaskCost','typicalNextEventDate','typicalSituation','multiTask','bomCode','bomCost','bomStock','maxPartsDeliveryTimeInBom','totalCost','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




class BomAndTaskAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','bomCode','taskCode','bomAndTaskSet','bomAndTaskSetCost',)
    search_fields = ('companyCode','companyName','plant','bomCode','taskCode','bomAndTaskSet','bomAndTaskSetCost',)
    list_filter = ('companyCode','companyName','plant','bomCode','taskCode','bomAndTaskSet','bomAndTaskSetCost',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定





# 以下でadminサイトに表示させる
admin.site.register(MasterDataTable,MasterDataTableAdmin)
admin.site.register(BomAndTask,BomAndTaskAdmin)


