from django.contrib import admin
from .models import JunctionTable

class JunctionTableAdmin(admin.ModelAdmin):
    list_display = ('taskCode','taskCost', 'bomCode', 'bomCost',)
    search_fields = ('taskCode','taskCost', 'bomCode', 'bomCost',)
    list_filter = ('taskCode',) # adminで右側にあるフィルターBOXのこと
    ordering = ('taskCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定
# 以下でadminサイトに表示させる
admin.site.register(JunctionTable,JunctionTableAdmin)
