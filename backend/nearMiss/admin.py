from django.contrib import admin
from .models import NearMiss,SafetyIndicators,TrendSafetyIndicators


class NearMissAdmin(admin.ModelAdmin):
    list_display = ('companyCode','userName', 'nearMissNo', 'department','dateOfOccurrence','placeOfOccurrence','typeOfAccident','description','factor','injuredLv','equipmentDamageLv','affectOfEnviroment','newsCoverage','measures','actionItems','solvedActionItems','createdDay','updateDay')
    readonly_fields = ('nearMissNo','measures','createdDay','updateDay') 
    search_fields = ('companyCode','userName', 'nearMissNo', 'department','dateOfOccurrence','placeOfOccurrence','typeOfAccident','description','factor','injuredLv','equipmentDamageLv','affectOfEnviroment','newsCoverage','measures','actionItems','solvedActionItems','createdDay','updateDay')
    list_filter = ('companyCode',"userName",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




class SafetyIndicatorsAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'safetyIndicators', 'dangerArea','totalOfNearMiss', 'countOfLevelA', 'rateOflevelA', 'countOfActionItems', 'countOfSolvedActionItems', 'rateOfActionItems')
    readonly_fields = ('safetyIndicators','totalOfNearMiss', 'countOfLevelA', 'rateOflevelA', 'countOfActionItems', 'countOfSolvedActionItems', 'rateOfActionItems') 
    search_fields = ('companyCode', 'companyName', 'safetyIndicators', 'dangerArea','totalOfNearMiss', 'countOfLevelA', 'rateOflevelA', 'countOfActionItems', 'countOfSolvedActionItems', 'rateOfActionItems')
    list_filter = ('companyCode','companyName',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class TrendSafetyIndicatorsAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'safetyIndicators', 'lastUpdateDay')
    readonly_fields = ( 'safetyIndicators', 'lastUpdateDay') 
    search_fields = ('companyCode', 'companyName', 'safetyIndicators', 'lastUpdateDay')
    list_filter = ('companyCode','companyName',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




# 以下でadminサイトに表示させる
admin.site.register(NearMiss,NearMissAdmin)
admin.site.register(SafetyIndicators,SafetyIndicatorsAdmin)
admin.site.register(TrendSafetyIndicators,TrendSafetyIndicatorsAdmin)
