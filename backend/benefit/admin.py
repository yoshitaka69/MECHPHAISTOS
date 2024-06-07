from django.contrib import admin
from .models import SimulationBenefit,ImprovementBenefti,RiskAvoidBenefit,PartsManagementBenefit




class CalTablePlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    readonly_fields = ('no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',) 
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


admin.site.register(SummedPlannedCost,SummedPlannedCostAdmin)
admin.site.register(SummedActualCost,SummedActualCostAdmin)
