from django.contrib import admin
from .models import MasterDataTable,BomAndTask,CeListAndTask,BadActorManagement,EventYearPPM,GapOfRepairingCost
from .models import Schedule

class MasterDataTableAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','ceListNo','equipment','machineName','taskPM02','countOfPM02','latestPM02','laborCostOfPM02','taskPM03','countOfPM03','latestPM03','laborCostOfPM03','taskPM04','countOfPM04','latestPM04','laborCostOfPM04','taskPM05','countOfPM05','latestPM05','laborCostOfPM05','typicalTaskName','typicalConstPeriod','typicalTaskCost','typicalNextEventDate','typicalSituation','multiTask','bomCode','bomCost','bomStock','maxPartsDeliveryTimeInBom','totalCost','levelSetValue','mttr','possibilityOfContinuousProduction','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later')
    search_fields = ('companyCode','companyName','plant','ceListNo','equipment','machineName','taskPM02','countOfPM02','latestPM02','laborCostOfPM02','taskPM03','countOfPM03','latestPM03','laborCostOfPM03','taskPM04','countOfPM04','latestPM04','laborCostOfPM04','taskPM05','countOfPM05','latestPM05','laborCostOfPM05','typicalTaskName','typicalConstPeriod','typicalTaskCost','typicalNextEventDate','typicalSituation','multiTask','bomCode','bomCost','bomStock','maxPartsDeliveryTimeInBom','totalCost','levelSetValue','mttr','possibilityOfContinuousProduction','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later')
    list_filter = ('companyCode','companyName','plant','ceListNo','equipment','machineName','taskPM02','countOfPM02','latestPM02','laborCostOfPM02','taskPM03','countOfPM03','latestPM03','laborCostOfPM03','taskPM04','countOfPM04','latestPM04','laborCostOfPM04','taskPM05','countOfPM05','latestPM05','laborCostOfPM05','typicalTaskName','typicalConstPeriod','typicalTaskCost','typicalNextEventDate','typicalSituation','multiTask','bomCode','bomCost','bomStock','maxPartsDeliveryTimeInBom','totalCost','levelSetValue','mttr','possibilityOfContinuousProduction','impactForProduction','probabilityOfFailure','assessment','rcaOrReplace','sparePartsOrAlternative','coveredFromTask','twoways','ceDescription','thisYear10ago','thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago','thisYear','thisYear1later','thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later') # adminで右側にあるフィルターBOXのこと
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





class CeListAndTaskAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName', 'plant', 'equipment', 'machine', 'no1HighLevelMachine', 'no1HighPriorityTaskName', 'no2HighLevelMachine', 'no2HighPriorityTaskName','no3HighLevelMachine', 'no3HighPriorityTaskName','no4HighLevelMachine', 'no4HighPriorityTaskName','no5HighLevelMachine', 'no5HighPriorityTaskName','no6HighLevelMachine', 'no6HighPriorityTaskName','no17HighLevelMachine', 'no7HighPriorityTaskName','no8HighLevelMachine', 'no8HighPriorityTaskName','no9HighLevelMachine', 'no9HighPriorityTaskName','no10HighLevelMachine', 'no10HighPriorityTaskName', )
    search_fields = ('companyCode','companyName', 'plant', 'equipment', 'machine', 'no1HighLevelMachine', 'no1HighPriorityTaskName', 'no2HighLevelMachine', 'no2HighPriorityTaskName','no3HighLevelMachine', 'no3HighPriorityTaskName','no4HighLevelMachine', 'no4HighPriorityTaskName','no5HighLevelMachine', 'no5HighPriorityTaskName','no6HighLevelMachine', 'no6HighPriorityTaskName','no17HighLevelMachine', 'no7HighPriorityTaskName','no8HighLevelMachine', 'no8HighPriorityTaskName','no9HighLevelMachine', 'no9HighPriorityTaskName','no10HighLevelMachine', 'no10HighPriorityTaskName',)
    list_filter = ('companyCode','companyName', 'plant', 'equipment', 'machine', 'no1HighLevelMachine', 'no1HighPriorityTaskName', 'no2HighLevelMachine', 'no2HighPriorityTaskName','no3HighLevelMachine', 'no3HighPriorityTaskName','no4HighLevelMachine', 'no4HighPriorityTaskName','no5HighLevelMachine', 'no5HighPriorityTaskName','no6HighLevelMachine', 'no6HighPriorityTaskName','no17HighLevelMachine', 'no7HighPriorityTaskName','no8HighLevelMachine', 'no8HighPriorityTaskName','no9HighLevelMachine', 'no9HighPriorityTaskName','no10HighLevelMachine', 'no10HighPriorityTaskName', ) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class BadActorManagementAdmin(admin.ModelAdmin):

    list_display = ('companyCode', 'companyName', 'plant', 'equipment', 'badActor')
    search_fields = ('companyCode', 'companyName', 'plant', 'equipment', 'badActor')
    list_filter = ('companyCode', 'companyName', 'plant', 'equipment', 'badActor' ) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class EventYearPPMAdmin(admin.ModelAdmin):

    list_display = ('companyCode', 'companyName', 'plant', 'equipment', 'machine','PPM10YearCostAgo', 'PPM9YearCostAgo', 'PPM8YearCostAgo' ,'PPM7YearCostAgo' , 'PPM6YearCostAgo' ,'PPM5YearCostAgo', 'PPM4YearCostAgo', 'PPM3YearCostAgo', 'PPM2YearCostAgo', 'PPM1YearCostAgo', 'PPM10YearCost','PPM0YearCost', 'PPM1YearCost', 'PPM2YearCost' ,'PPM3YearCost' , 'PPM4YearCost' ,'PPM5YearCost', 'PPM6YearCost', 'PPM7YearCost', 'PPM8YearCost', 'PPM9YearCost', 'PPM10YearCost')
    search_fields = ('companyCode', 'companyName', 'plant', 'equipment', 'machine','PPM10YearCostAgo', 'PPM9YearCostAgo', 'PPM8YearCostAgo' ,'PPM7YearCostAgo' , 'PPM6YearCostAgo' ,'PPM5YearCostAgo', 'PPM4YearCostAgo', 'PPM3YearCostAgo', 'PPM2YearCostAgo', 'PPM1YearCostAgo', 'PPM10YearCost','PPM0YearCost', 'PPM1YearCost', 'PPM2YearCost' ,'PPM3YearCost' , 'PPM4YearCost' ,'PPM5YearCost', 'PPM6YearCost', 'PPM7YearCost', 'PPM8YearCost', 'PPM9YearCost', 'PPM10YearCost')
    list_filter = ('companyCode', 'companyName', 'plant', 'equipment', 'machine','PPM10YearCostAgo', 'PPM9YearCostAgo', 'PPM8YearCostAgo' ,'PPM7YearCostAgo' , 'PPM6YearCostAgo' ,'PPM5YearCostAgo', 'PPM4YearCostAgo', 'PPM3YearCostAgo', 'PPM2YearCostAgo', 'PPM1YearCostAgo', 'PPM10YearCost','PPM0YearCost', 'PPM1YearCost', 'PPM2YearCost' ,'PPM3YearCost' , 'PPM4YearCost' ,'PPM5YearCost', 'PPM6YearCost', 'PPM7YearCost', 'PPM8YearCost', 'PPM9YearCost', 'PPM10YearCost') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




class GapOfRepairingCostAdmin(admin.ModelAdmin):

    list_display = ('companyCode', 'companyName', 'plant', 'equipment', 'machine','GapCostPPM10Ago','GapCostPPM9Ago','GapCostPPM8Ago','GapCostPPM7Ago','GapCostPPM6Ago','GapCostPPM5Ago','GapCostPPM4Ago','GapCostPPM3Ago','GapCostPPM2Ago','GapCostPPM1Ago', 'GapCostPPM0', 'GapCostPPM1','GapCostPPM2','GapCostPPM3','GapCostPPM4','GapCostPPM5','GapCostPPM6','GapCostPPM7','GapCostPPM8','GapCostPPM9','GapCostPPM10')
    search_fields = ('companyCode', 'companyName', 'plant', 'equipment', 'machine','GapCostPPM10Ago','GapCostPPM9Ago','GapCostPPM8Ago','GapCostPPM7Ago','GapCostPPM6Ago','GapCostPPM5Ago','GapCostPPM4Ago','GapCostPPM3Ago','GapCostPPM2Ago','GapCostPPM1Ago', 'GapCostPPM0', 'GapCostPPM1','GapCostPPM2','GapCostPPM3','GapCostPPM4','GapCostPPM5','GapCostPPM6','GapCostPPM7','GapCostPPM8','GapCostPPM9','GapCostPPM10')
    list_filter = ('companyCode', 'companyName', 'plant', 'equipment', 'machine','GapCostPPM10Ago','GapCostPPM9Ago','GapCostPPM8Ago','GapCostPPM7Ago','GapCostPPM6Ago','GapCostPPM5Ago','GapCostPPM4Ago','GapCostPPM3Ago','GapCostPPM2Ago','GapCostPPM1Ago', 'GapCostPPM0', 'GapCostPPM1','GapCostPPM2','GapCostPPM3','GapCostPPM4','GapCostPPM5','GapCostPPM6','GapCostPPM7','GapCostPPM8','GapCostPPM9','GapCostPPM10') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置


    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'pmType', 'startDate', 'endDate')  # 管理画面に表示するフィールド
    search_fields = ('name', 'pmType')  # 検索可能なフィールド
    list_filter = ('pmType', 'startDate')  # フィルタリングできるフィールド





# 以下でadminサイトに表示させる
admin.site.register(MasterDataTable,MasterDataTableAdmin)
admin.site.register(BomAndTask,BomAndTaskAdmin)
admin.site.register(CeListAndTask,CeListAndTaskAdmin)
admin.site.register(BadActorManagement,BadActorManagementAdmin)
admin.site.register(EventYearPPM,EventYearPPMAdmin)
admin.site.register(GapOfRepairingCost,GapOfRepairingCostAdmin)
admin.site.register(Schedule,ScheduleAdmin)

