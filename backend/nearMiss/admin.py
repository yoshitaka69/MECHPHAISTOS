from django.contrib import admin
from .models import NearMiss

# 以下でadminサイトに表示させる
admin.site.register(NearMiss)