from django.contrib import admin
from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05,
class PlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','jan','fab','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','commitment',)
    search_fields = ('companyCode','companyName','plant','plannedMonth','plannedCost',)
    list_filter = ('companyCode','companyName','plant','plannedMonth','plannedCost',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

class ActualPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualMonth','actualCost',)
    search_fields = ('companyCode','companyName','plant','actualMonth','actualCost',)
    list_filter = ('companyCode','companyName','plant','actualMonth','actualCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','plannedMonth','plannedCost',)
    search_fields = ('companyCode','companyName','plant','plannedMonth','plannedCost',)
    list_filter = ('companyCode','companyName','plant','plannedMonth','plannedCost',) 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 


class ActualPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualMonth','actualCost',)
    search_fields = ('companyCode','companyName','plant','actualMonth','actualCost',)
    list_filter = ('companyCode','companyName','plant','actualMonth','actualCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class ActualPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualMonth','actualCost',)
    search_fields = ('companyCode','companyName','plant','actualMonth','actualCost',)
    list_filter = ('companyCode','companyName','plant','actualMonth','actualCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class PlannedPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','plannedMonth','plannedCost')
    search_fields = ('companyCode','companyName','plant','plannedMonth','plannedCost')
    list_filter = ('companyCode','companyName','plant','plannedMonth','plannedCost') 
    ordering = ('companyCode',) 
    save_on_top = True 

    list_per_page = 50 

class ActualPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','actualMonth','actualCost',)
    search_fields = ('companyCode','companyName','plant','actualMonth','actualCost',)
    list_filter = ('companyCode','companyName','plant','actualMonth','actualCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class IndexFormPM02Admin(admin.ModelAdmin):
    list_display = ('indexNamePM02',)
    search_fields = ('indexNamePM02',)
    list_filter = ('indexNamePM02',)
    ordering = ('indexNamePM02',)
    save_on_top = True

    list_per_page = 50 


class IndexFormPM03Admin(admin.ModelAdmin):
    list_display = ('indexNamePM03',)
    search_fields = ('indexNamePM03',)
    list_filter = ('indexNamePM03',)
    ordering = ('indexNamePM03',)
    save_on_top = True

    list_per_page = 50 


class IndexFormPM04Admin(admin.ModelAdmin):
    list_display = ('indexNamePM04',)
    search_fields = ('indexNamePM04',)
    list_filter = ('indexNamePM04',)
    ordering = ('indexNamePM04',)
    save_on_top = True


    list_per_page = 50 

class IndexFormPM05Admin(admin.ModelAdmin):
    list_display = ('indexNamePM05',)
    search_fields = ('indexNamePM05',)
    list_filter = ('indexNamePM05',)
    ordering = ('indexNamePM05',)
    save_on_top = True

    list_per_page = 50 


class CalculationTablePM02Admin(admin.ModelAdmin):
    list_display = ('indexPM02', 'cost',)
    search_fields = ('indexPM02', 'cost',)
    list_filter = ('indexPM02', 'cost',)
    ordering = ('indexPM02',)
    save_on_top = True
    list_per_page = 50 


class CalculationTablePM03Admin(admin.ModelAdmin):
    list_display = ('indexPM03', 'cost',)
    search_fields = ('indexPM03', 'cost',)
    list_filter = ('indexPM03', 'cost',)
    ordering = ('indexPM03',)
    save_on_top = True
    list_per_page = 50 


class CalculationTablePM04Admin(admin.ModelAdmin):
    list_display = ('indexPM04', 'cost',)
    search_fields = ('indexPM04', 'cost',)
    list_filter = ('indexPM04', 'cost',)
    ordering = ('indexPM04',)
    save_on_top = True
    list_per_page = 50 


class CalculationTablePM05Admin(admin.ModelAdmin):
    list_display = ('indexPM05', 'cost',)
    search_fields = ('indexPM05', 'cost',)
    list_filter = ('indexPM05', 'cost',)
    ordering = ('indexPM05',)
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

admin.site.register(IndexFormPM02,IndexFormPM02Admin)
admin.site.register(IndexFormPM03,IndexFormPM03Admin)
admin.site.register(IndexFormPM04,IndexFormPM04Admin)
admin.site.register(IndexFormPM05,IndexFormPM05Admin)


admin.site.register(CalculationTablePM02,CalculationTablePM02Admin)
admin.site.register(CalculationTablePM03,CalculationTablePM03Admin)
admin.site.register(CalculationTablePM04,CalculationTablePM04Admin)
admin.site.register(CalculationTablePM05,CalculationTablePM05Admin)