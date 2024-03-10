from django.contrib import admin
from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas

class Co2Admin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'plant', 'date', 'co2Cost', )
    search_fields = ('companyCode', 'companyName', 'plant', 'date', 'co2Cost', )
    list_filter = ('companyCode','companyName',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

class StmAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName', 'plant', 'date', 'stmCost', )
    search_fields = ('companyCode', 'companyName', 'plant', 'date', 'stmCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

class ElecAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName',  'plant', 'date', 'elecCost', )
    search_fields = ('companyCode', 'companyName', 'plant', 'date', 'elecCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

class CompAirAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName', 'plant', 'date', 'compAirCost', )
    search_fields = ('companyCode', 'companyName','plant', 'date', 'compAirCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )


class WellWaterAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'plant', 'date', 'wellWaterCost', )
    search_fields = ('companyCode', 'companyName', 'plant', 'date', 'wellWaterCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

class PureWaterAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName',  'plant', 'date', 'pureWaterCost', )
    search_fields = ('companyCode', 'companyName', 'plant', 'date', 'pureWaterCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

class WwtAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'plant', 'date', 'wwtCost', )
    search_fields = ('companyCode','companyName',  'plant', 'date', 'wwtCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

class ExtGasAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'plant', 'date', 'exhaustGasCost', )
    search_fields = ('companyCode', 'companyName', 'plant', 'date', 'exhaustGasCost', )
    list_filter = ('companyCode','companyName', ) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode', )

# 以下でadminサイトに表示させる
admin.site.register(Co2,Co2Admin)
admin.site.register(Stm,StmAdmin)
admin.site.register(ElectricityUsage,ElecAdmin)
admin.site.register(CompressedAir,CompAirAdmin)
admin.site.register(WellWater,WellWaterAdmin)
admin.site.register(PureWater,PureWaterAdmin)
admin.site.register(Wwt,WwtAdmin)
admin.site.register(ExhaustGas,ExtGasAdmin)
