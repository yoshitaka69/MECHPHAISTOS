from django.contrib import admin
from .models import Co2,Stm,ElectricityUsage,CompressedAir,WellWater,PureWater,Wwt,ExhaustGas

# 以下でadminサイトに表示させる
admin.site.register(Co2)
admin.site.register(Stm)
admin.site.register(ElectricityUsage)
admin.site.register(CompressedAir)
admin.site.register(WellWater)
admin.site.register(PureWater)
admin.site.register(Wwt)
admin.site.register(ExhaustGas)
