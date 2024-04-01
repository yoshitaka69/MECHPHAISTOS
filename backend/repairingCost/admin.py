from django.contrib import admin
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05
class PlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

class ActualPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 


class ActualPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class ActualPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 

class ActualPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    search_fields = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    list_filter = ('companyCode','companyName','plant','year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment','totalCost',)
    ordering = ('companyCode',)
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

