from django.contrib import admin
from .models import TaskList

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','taskCode', 'taskOfPM','typeOfMaintenance')
    search_fields = ('companyCode','companyName','taskCode', 'taskOfPM','typeOfMaintenance')
    list_filter = ('companyCode','companyName',"taskCode",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置
    #readonly_fields = ("title", )  あとでreadonlyのやつだとかを入れる予定。20240305 y.noto

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

admin.site.register(TaskList,TaskListAdmin)

