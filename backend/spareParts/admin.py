from django.contrib import admin
from .models import SpareParts,Category,Location,Classification


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','description',)
    search_fields = ('category','description',)
    list_filter = ('category','description',) # adminで右側にあるフィルターBOXのこと
    ordering = ('category',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class LocationAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','location_Id','location',)
    search_fields = ('companyCode','companyName','location_Id','location',)
    list_filter = ('companyCode','companyName','location_Id','location',) # adminで右側にあるフィルターBOXのこと
    ordering = ('location_Id',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification','description',)
    search_fields = ('classification','description',)
    list_filter = ('classification','description',) # adminで右側にあるフィルターBOXのこと
    ordering = ('classification',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



class SparePartsAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','partsName', 'category','bomCode',)
    search_fields = ('companyCode','companyName', 'partsName', 'category','bomCode',)
    list_filter = ('companyCode','companyName','partsName', 'category','bomCode',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


admin.site.register(SpareParts,SparePartsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Classification,ClassificationAdmin)