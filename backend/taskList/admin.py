from django.contrib import admin
from .models import TaskListPPM02,TaskListAPM02,TaskListPPM03,TaskListAPM03,TaskListAPM04,TaskListPPM05,TaskListAPM05,TypicalTaskList,TaskList


#PPM02
class TaskListPPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','ceListNo','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM02', 'countOfPPM02', 'latestPPM02', 'periodOfPPM02',  'pM02Content', 'maintenanceCategory','nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',)
    search_fields = ('companyCode','companyName','ceListNo','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM02', 'countOfPPM02', 'latestPPM02', 'periodOfPPM02',  'pM02Content','maintenanceCategory', 'nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',)
    list_filter = ('companyCode','companyName','ceListNo','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM02', 'countOfPPM02', 'latestPPM02', 'periodOfPPM02',  'pM02Content', 'maintenanceCategory','nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


#APM02
class TaskListAPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM02', 'startDateAPM02', 'endDateAPM02', 'constructionPeriod', 'description')
    search_fields = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM02', 'startDateAPM02', 'endDateAPM02', 'constructionPeriod', 'description')
    list_filter = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM02', 'startDateAPM02', 'endDateAPM02', 'constructionPeriod', 'description') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



#PPM03
class TaskListPPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','ceListNo','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM03', 'countOfPPM03', 'latestPPM03', 'periodOfPPM03', 'pM03Content', 'maintenanceCategory','nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',)
    search_fields = ('companyCode','companyName','ceListNo','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM03', 'countOfPPM03', 'latestPPM03', 'periodOfPPM03', 'pM03Content', 'maintenanceCategory','nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',)
    list_filter = ('companyCode','companyName','ceListNo','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM03', 'countOfPPM03', 'latestPPM03', 'periodOfPPM03', 'pM03Content', 'maintenanceCategory','nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定


#APM03
class TaskListAPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM03', 'startDateAPM03', 'endDateAPM03', 'constructionPeriod', 'description')
    search_fields = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM03', 'startDateAPM03', 'endDateAPM03', 'constructionPeriod', 'description')
    list_filter = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM03', 'startDateAPM03', 'endDateAPM03', 'constructionPeriod', 'description') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



#APM04
class TaskListAPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM04', 'countOfAPM04', 'latestAPM04', 'constructionPeriod')
    search_fields = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM04', 'countOfAPM04', 'latestAPM04', 'constructionPeriod')
    list_filter = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM04', 'countOfAPM04', 'latestAPM04', 'constructionPeriod') # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定



#PPM05
class TaskListPPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM05', 'countOfPPM05', 'latestPPM05', 'periodOfPPM05', 'nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',)
    search_fields = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM05', 'countOfPPM05', 'latestPPM05', 'periodOfPPM05', 'nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',)
    list_filter = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfPPM05', 'countOfPPM05', 'latestPPM05', 'periodOfPPM05', 'nextEventDate', 'situation', 'thisYear10ago', 'thisYear9ago','thisYear8ago','thisYear7ago','thisYear6ago','thisYear5ago','thisYear4ago','thisYear3ago','thisYear2ago','thisYear1ago', 'thisYear', 'thisYear1later', 'thisYear2later','thisYear3later','thisYear4later','thisYear5later','thisYear6later','thisYear7later','thisYear8later','thisYear9later','thisYear10later',) # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',) # 表示する順番
    save_on_top = True #上部にもsaveボタンを配置

    list_per_page = 50 # １ページあたりに表示するオブジェクト数を指定

#APM05
class TaskListAPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM05', 'startDateAPM05', 'endDateAPM05', 'constructionPeriod', 'description')
    search_fields = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM05', 'startDateAPM05', 'endDateAPM05', 'constructionPeriod', 'description')
    list_filter = ('companyCode','companyName','plant', 'equipment', 'machineName', 'taskCode', 'taskName', 'laborCostOfAPM05', 'startDateAPM05', 'endDateAPM05', 'constructionPeriod', 'description') # adminで右側にあるフィルターBOXのこと
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



#-------------------------------------------------------------------------------
from django.contrib import admin
from django.db import models  # models をインポート
from .models import TaskList  # TaskList モデルのインポート

class TaskListAdmin(admin.ModelAdmin):
    # list_display, search_fields にすべてのフィールドを自動で設定
    def get_list_display(self, request):
        # '__all__' の代わりにモデルの全フィールドを取得して表示
        return [field.name for field in self.model._meta.fields]

    def get_search_fields(self, request):
        # 全ての CharField と TextField を検索フィールドに追加
        search_fields = [
            field.name for field in self.model._meta.fields
            if isinstance(field, (models.CharField, models.TextField))
        ]
        return search_fields

    list_filter = ('companyCode',)  # adminで右側にあるフィルターBOXのこと
    ordering = ('companyCode',)  # 表示する順番
    save_on_top = True  # 上部にもsaveボタンを配置
    list_per_page = 50  # １ページあたりに表示するオブジェクト数


#-------------------------------------------------------------------------------


admin.site.register(TaskListPPM02,TaskListPPM02Admin)
admin.site.register(TaskListAPM02,TaskListAPM02Admin)

admin.site.register(TaskListPPM03,TaskListPPM03Admin)
admin.site.register(TaskListAPM03,TaskListAPM03Admin)

admin.site.register(TaskListAPM04,TaskListAPM04Admin)

admin.site.register(TaskListPPM05,TaskListPPM05Admin)
admin.site.register(TaskListAPM05,TaskListAPM05Admin)


admin.site.register(TypicalTaskList,TypicalTaskListAdmin)
admin.site.register(TaskList,TaskListAdmin)

