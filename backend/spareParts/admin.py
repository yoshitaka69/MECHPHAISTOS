from django.contrib import admin
from .models import SpareParts,BomList,SparePartsManagement


class SparePartsAdmin(admin.ModelAdmin):

    list_display = ('companyCode','companyName','plant','equipment','machineName','image','bomCode','partsNo','partsName','partsModel','serialNumber','category','partsCost','numberOf','summedPartsCost','unit','location','stock','partsDeliveryTime','classification','partsDescription')
    search_fields = ('companyCode','companyName','plant','equipment','machineName','image','bomCode','partsNo','partsName','partsModel','serialNumber','category','partsCost','numberOf','summedPartsCost','unit','location','stock','partsDeliveryTime','classification','partsDescription')
    list_filter = ('companyCode','companyName','plant','equipment','machineName','image','bomCode','partsNo','partsName','partsModel','serialNumber','category','partsCost','numberOf','summedPartsCost','unit','location','stock','partsDeliveryTime','classification','partsDescription') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class BomListAdmin(admin.ModelAdmin):
    list_display = ('bomCode','bomCost', 'maxPartsDeliveryTimeInBom')
    search_fields = ('bomCode','bomCost', 'maxPartsDeliveryTimeInBom')
    list_filter = ('bomCode','bomCost', 'maxPartsDeliveryTimeInBom') # adminで右側にあるフィルターBOXのこと
    ordering = ('bomCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




class SparePartsManagementAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment','machineName','totalSparePartsCost','inventoryTurnover')
    readonly_fields = ('totalSparePartsCost','inventoryTurnover',) 
    search_fields = ('companyCode','companyName','plant', 'equipment','machineName','totalSparePartsCost','inventoryTurnover')
    list_filter = ('companyCode','companyName','plant', 'equipment','machineName','totalSparePartsCost','inventoryTurnover') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



admin.site.register(SpareParts,SparePartsAdmin)
admin.site.register(BomList,BomListAdmin)
admin.site.register(SparePartsManagement,SparePartsManagementAdmin)
