from django.contrib import admin
from .models import Company, CeList

# 以下でadminサイトに表示させる


admin.site.register(Company)
admin.site.register(CeList)