from django.contrib import admin
from .models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05,TypicalTaskList,TaskList

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



class TypicalTaskListAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskCode', 'typicalTaskName', 'typicalTaskCost', 'typicalLatestDate', 'typicalConstPeriod', 'typicalNextEventDate', 'multiTasking', 'typicalSituation')
    search_fields = ('companyCode', 'taskCode', 'typicalTaskName', 'typicalTaskCost', 'typicalLatestDate', 'typicalConstPeriod', 'typicalNextEventDate', 'multiTasking', 'typicalSituation')
    list_filter = ('companyCode', "taskCode",) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定




class TaskListAdmin(admin.ModelAdmin):
    list_display = ('companyCode','plant', 'equipment', 'machineName', 'taskListNo', 'typicalLatestDate', 'typicalTaskName', 'typicalTaskCost', 'typicalConstPeriod', 'multiTasking', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomCost', 'totalCost', 'thisYear', 'thisYear1later', 'thisYear2later', 'thisYear3later', 'thisYear4later', 'thisYear5later', 'thisYear6later', 'thisYear7later', 'thisYear8later', 'thisYear9later', 'thisYear10later',)
    search_fields = ('companyCode','plant', 'equipment', 'machineName', 'taskListNo', 'typicalLatestDate', 'typicalTaskName', 'typicalTaskCost', 'typicalConstPeriod', 'multiTasking', 'typicalNextEventDate', 'typicalSituation', 'bomCode', 'bomCost', 'totalCost', 'thisYear', 'thisYear1later', 'thisYear2later', 'thisYear3later', 'thisYear4later', 'thisYear5later', 'thisYear6later', 'thisYear7later', 'thisYear8later', 'thisYear9later', 'thisYear10later', )
    list_filter = ('companyCode',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



admin.site.register(TaskListPM02,TaskListPM02Admin)
admin.site.register(TaskListPM03,TaskListPM03Admin)
admin.site.register(TaskListPM04,TaskListPM04Admin)
admin.site.register(TaskListPM05,TaskListPM05Admin)

admin.site.register(TypicalTaskList,TypicalTaskListAdmin)
admin.site.register(TaskList,TaskListAdmin)

