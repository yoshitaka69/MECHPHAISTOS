from django.contrib import admin
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05

class PlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','plannedPM02','no1PlannedPM02','totalPlannedPM02',)
    search_fields = ('companyCode','companyName','plant','plannedPM02','no1PlannedPM02','totalPlannedPM02',)
    list_filter = ('companyCode','companyName','plant','plannedPM02','no1PlannedPM02','totalPlannedPM02',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

class ActualPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualPM02','no1ActualPM02','totalActualPM02',)
    search_fields = ('companyCode','companyName','plant','actualPM02','no1ActualPM02','totalActualPM02')
    list_filter = ('companyCode','companyName','plant','actualPM02','no1ActualPM02','totalActualPM02')
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','plannedPM03','no1PlannedPM03','totalPlannedPM03',)
    search_fields = ('companyCode','companyName','plant','plannedPM03','no1PlannedPM03','totalPlannedPM03',)
    list_filter = ('companyCode','companyName','plant','plannedPM03','no1PlannedPM03','totalPlannedPM03',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 


class ActualPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualPM03','no1ActualPM03','totalActualPM03',)
    search_fields = ('companyCode','companyName','plant','actualPM03','no1ActualPM03','totalActualPM03')
    list_filter = ('companyCode','companyName','plant','actualPM03','no1ActualPM03','totalActualPM03')
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class ActualPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualPM04','no1ActualPM04','totalActualPM04',)
    search_fields = ('companyCode','companyName','plant','actualPM04','no1ActualPM04','totalActualPM04')
    list_filter = ('companyCode','companyName','plant','actualPM04','no1ActualPM04','totalActualPM04')
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','plannedPM05','no1PlannedPM05','totalPlannedPM05',)
    search_fields = ('companyCode','companyName','plant','plannedPM05','no1PlannedPM05','totalPlannedPM05',)
    list_filter = ('companyCode','companyName','plant','plannedPM05','no1PlannedPM05','totalPlannedPM05',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 

class ActualPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualPM05','no1ActualPM05','totalActualPM05',)
    search_fields = ('companyCode','companyName','plant','actualPM05','no1ActualPM05','totalActualPM05')
    list_filter = ('companyCode','companyName','plant','actualPM05','no1ActualPM05','totalActualPM05')
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
