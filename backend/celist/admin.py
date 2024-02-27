from django.contrib import admin
from .models import Ce,SpareParts,Task

# 以下でadminサイトに表示させる
admin.site.register(Ce)
admin.site.register(SpareParts)
admin.site.register(Task)