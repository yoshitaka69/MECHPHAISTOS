from django.contrib import admin
from .models import MasterDataTable

class MasterDataTableAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','ceList_Id','equipment','machineName','taskCode','taskName','typeOfPM','laborCostOfPM','countOfPM','latestPM','periodOfPM','bomCode','maxPartsDeliveryTimeInBom','constructionPeriod','nextEventDate','situation','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later')
    search_fields = ('companyCode','companyName','plant','ceList_Id','equipment','machineName','taskCode','taskName','typeOfPM','laborCostOfPM','countOfPM','latestPM','periodOfPM','bomCode','maxPartsDeliveryTimeInBom','constructionPeriod','nextEventDate','situation','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later')
    list_filter = ('companyCode','companyName','plant','ceList_Id','equipment','machineName','taskCode','taskName','typeOfPM','laborCostOfPM','countOfPM','latestPM','periodOfPM','bomCode','maxPartsDeliveryTimeInBom','constructionPeriod','nextEventDate','situation','levelSetValue','mttr','possibilityOfProductionLv','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


# 以下でadminサイトに表示させる
admin.site.register(MasterDataTable,MasterDataTableAdmin)
