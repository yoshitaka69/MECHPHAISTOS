from django.contrib import admin
from .models import Company,User,Payment

# 以下でadminサイトに表示させる
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Payment)
