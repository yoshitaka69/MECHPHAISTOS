from django.contrib import admin
from .models import NearMiss,SafetyIndicators


class NearMissAdmin(admin.ModelAdmin):
    list_display = ('companyCode','userName', 'department', 'dateOfOccurrence','createdDay')
    search_fields = ('companyCode','userName','department', 'dateOfOccurrence')
    list_filter = ('companyCode',"userName",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




class SafetyIndicatorsAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName', 'safetyIndicators', 'totalOfNearMiss','rateOflevelA', 'ActionItems', 'solvedActionItems', 'rateOfActionItems')
    search_fields = ('companyCode','companyName', 'safetyIndicators', 'totalOfNearMiss','rateOflevelA', 'ActionItems', 'solvedActionItems', 'rateOfActionItems')
    list_filter = ('companyCode','companyName',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



# 以下でadminサイトに表示させる
admin.site.register(NearMiss,NearMissAdmin)
admin.site.register(SafetyIndicators,SafetyIndicatorsAdmin)
