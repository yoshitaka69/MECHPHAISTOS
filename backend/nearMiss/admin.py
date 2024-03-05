from django.contrib import admin
from .models import NearMiss


class NearMissAdmin(admin.ModelAdmin):
    list_display = ('companyCode','userName', 'department', 'dateOfOccurrence','createdDay')
    search_fields = ('companyCode','userName','department', 'dateOfOccurrence')
    list_filter = ('companyCode',"userName",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

# 以下でadminサイトに表示させる
admin.site.register(NearMiss,NearMissAdmin)