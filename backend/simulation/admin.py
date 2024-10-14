from django.contrib import admin
from .models import No1Simulation, No2Simulation, No3Simulation

@admin.register(No1Simulation)
class No1SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'PMType', 'typicalLatestDate', 'taskOfPeriod', 'totalLaborCost', 'bomCode', 'bomCost')
    search_fields = ('taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName')

@admin.register(No2Simulation)
class No2SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'PMType', 'typicalLatestDate', 'taskOfPeriod', 'totalLaborCost', 'bomCode', 'bomCost')
    search_fields = ('taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName')

@admin.register(No3Simulation)
class No3SimulationAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName', 'PMType', 'typicalLatestDate', 'taskOfPeriod', 'totalLaborCost', 'bomCode', 'bomCost')
    search_fields = ('taskListNo', 'typicalTaskName', 'plant', 'equipment', 'machineName')
