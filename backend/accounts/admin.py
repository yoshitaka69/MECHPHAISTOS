from django.contrib import admin
from .models import CompanyList,UserList,PaymentsList

# 以下でadminサイトに表示させる
admin.site.register(CompanyList)
admin.site.register(UserList)
admin.site.register(PaymentsList)
