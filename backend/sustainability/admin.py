from django.contrib import admin
from .models import Co2List,StmList,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas

# 以下でadminサイトに表示させる
admin.site.register(Co2List)
admin.site.register(StmList)
admin.site.register(ElectricityUsage)
admin.site.register(CompressedAir)
admin.site.register(WellWater)
admin.site.register(PureWater)
admin.site.register(Wwt)
admin.site.register(ExhaustGas)

