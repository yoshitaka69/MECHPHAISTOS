from django.contrib import admin
from .models import SpareParts

class SparePartsAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','partsName', 'category','bomCode',)
    search_fields = ('companyCode','companyName','plant', 'partsName', 'category','bomCode',)
    list_filter = ('companyCode','companyName','plant','partsName', 'category','bomCode',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置\

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


admin.site.register(SpareParts,SparePartsAdmin)