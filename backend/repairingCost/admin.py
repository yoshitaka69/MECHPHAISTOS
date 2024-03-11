from django.contrib import admin
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05,CalTablePlannedPM02,CalTableActualPM02,CalTablePlannedPM03,CalTableActualPM03,CalTableActualPM04,CalTablePlannedPM05,CalTableActualPM05
class PlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

class ActualPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 


class ActualPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class ActualPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM05Admin(admin.ModelAdmin):
    list_display = ('plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 

class ActualPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    list_filter = ('companyCode','companyName','plant','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class CalTablePlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTabelActualPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTablePlannedPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 



class CalTabelActualPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTabelActualPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTablePlannedPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTabelActualPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    search_fields = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    list_filter = ('companyCode','companyName','plant','totalCost','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost')
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 




# 以下でadminサイトに表示させる
admin.site.register(PlannedPM02,PlannedPM02Admin)
admin.site.register(ActualPM02,ActualPM02Admin)

admin.site.register(PlannedPM03,PlannedPM03Admin)
admin.site.register(ActualPM03,ActualPM03Admin)

admin.site.register(ActualPM04,ActualPM04Admin)

admin.site.register(PlannedPM05,PlannedPM05Admin)
admin.site.register(ActualPM05,ActualPM05Admin)

admin.site.register(CalTablePlannedPM02,CalTablePlannedPM02Admin)
admin.site.register(CalTableActualPM02,CalTabelActualPM02Admin)
admin.site.register(CalTablePlannedPM03,CalTablePlannedPM03Admin)
admin.site.register(CalTableActualPM03,CalTabelActualPM03Admin)
admin.site.register(CalTableActualPM04,CalTabelActualPM04Admin)
admin.site.register(CalTablePlannedPM05,CalTablePlannedPM05Admin)
admin.site.register(CalTableActualPM05,CalTabelActualPM05Admin)