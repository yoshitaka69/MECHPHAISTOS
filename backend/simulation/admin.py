from django.contrib import admin
from .models import BaseSimulation

@admin.register(BaseSimulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'typicalLatestDate', 'multiTasking', 'totalCost', 'taskOfPeriod')
    readonly_fields = ('typicalNextEventDate', 'typicalSituation', 'thisYear', 'thisYear1Later', 'thisYear2Later', 'thisYear3Later', 'thisYear4Later', 'thisYear5Later', 'thisYear6Later', 'thisYear7Later', 'thisYear8Later', 'thisYear9Later', 'thisYear10Later')


from django.contrib import admin
from .models import No1Simulation

@admin.register(No1Simulation)
class No1SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'typicalLatestDate', 'multiTasking', 'totalCost', 'taskOfPeriod')
    readonly_fields = ('typicalNextEventDate', 'typicalSituation', 'thisYear', 'thisYear1Later', 'thisYear2Later', 'thisYear3Later', 'thisYear4Later', 'thisYear5Later', 'thisYear6Later', 'thisYear7Later', 'thisYear8Later', 'thisYear9Later', 'thisYear10Later')


from .models import No2Simulation

@admin.register(No2Simulation)
class No2SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'typicalLatestDate', 'multiTasking', 'totalCost', 'taskOfPeriod')
    readonly_fields = ('typicalNextEventDate', 'typicalSituation', 'thisYear', 'thisYear1Later', 'thisYear2Later', 'thisYear3Later', 'thisYear4Later', 'thisYear5Later', 'thisYear6Later', 'thisYear7Later', 'thisYear8Later', 'thisYear9Later', 'thisYear10Later')



from django.contrib import admin
from .models import No3Simulation

@admin.register(No3Simulation)
class No3SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'typicalLatestDate', 'multiTasking', 'totalCost', 'taskOfPeriod')
    readonly_fields = ('typicalNextEventDate', 'typicalSituation', 'thisYear', 'thisYear1Later', 'thisYear2Later', 'thisYear3Later', 'thisYear4Later', 'thisYear5Later', 'thisYear6Later', 'thisYear7Later', 'thisYear8Later', 'thisYear9Later', 'thisYear10Later')