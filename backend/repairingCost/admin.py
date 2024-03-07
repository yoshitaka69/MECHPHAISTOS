from django.contrib import admin
from .models import Pm02,Pm03,Pm04,Pm05

class PM02Admin(admin.ModelAdmin):
    list_display = ('plant',)
    search_fields = ('plant',)
    list_filter = ('plant',) # adminで右側にあるフィルターBOXのこと
    ordering = ('plant',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定
# 以下でadminサイトに表示させる

class PM03Admin(admin.ModelAdmin):
    list_display = ('plant',)
    search_fields = ('plant',)
    list_filter = ('plant',) # adminで右側にあるフィルターBOXのこと
    ordering = ('plant',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定
# 以下でadminサイトに表示させる

class PM04Admin(admin.ModelAdmin):
    list_display = ('plant',)
    search_fields = ('plant',)
    list_filter = ('plant',) # adminで右側にあるフィルターBOXのこと
    ordering = ('plant',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定
# 以下でadminサイトに表示させる

class PM05Admin(admin.ModelAdmin):
    list_display = ('plant',)
    search_fields = ('plant',)
    list_filter = ('plant',) # adminで右側にあるフィルターBOXのこと
    ordering = ('plant',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定
# 以下でadminサイトに表示させる

# 以下でadminサイトに表示させる
admin.site.register(Pm02,PM02Admin)
admin.site.register(Pm03,PM03Admin)
admin.site.register(Pm04,PM04Admin)
admin.site.register(Pm05,PM05Admin)
