from django.contrib import admin
from .models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05

class TaskListPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','taskCode', )
    search_fields = ('companyCode','companyName','taskCode', )
    list_filter = ('companyCode','companyName',"taskCode",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class TaskListPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','taskCode', )
    search_fields = ('companyCode','companyName','taskCode', )
    list_filter = ('companyCode','companyName',"taskCode",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


class TaskListPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','taskCode', )
    search_fields = ('companyCode','companyName','taskCode', )
    list_filter = ('companyCode','companyName',"taskCode",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

class TaskListPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','taskCode', )
    search_fields = ('companyCode','companyName','taskCode', )
    list_filter = ('companyCode','companyName',"taskCode",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

admin.site.register(TaskListPM02,TaskListPM02Admin)
admin.site.register(TaskListPM03,TaskListPM03Admin)
admin.site.register(TaskListPM04,TaskListPM04Admin)
admin.site.register(TaskListPM05,TaskListPM05Admin)

