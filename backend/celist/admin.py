from django.contrib import admin
from .models import CeList,SparePartsList,TaskList

# 以下でadminサイトに表示させる
admin.site.register(CeList)
admin.site.register(SparePartsList)
admin.site.register(TaskList)