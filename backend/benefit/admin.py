from django.contrib import admin
from .models import SimulationBenefit,ImprovementBenefti,RiskAvoidBenefit,PartsManagementBenefit




class SimulationBenefitAdmin(admin.ModelAdmin):
    list_display = ('companyCode',)
    readonly_fields = ('companyCode',) 
    search_fields = ('companyCode',)
    list_filter = ('companyCode',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 


class SimulationBenefitAdmin(admin.ModelAdmin):
    list_display = ('companyCode',)
    readonly_fields = ('companyCode',) 
    search_fields = ('companyCode',)
    list_filter = ('companyCode',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 



class SimulationBenefitAdmin(admin.ModelAdmin):
    list_display = ('companyCode',)
    readonly_fields = ('companyCode',) 
    search_fields = ('companyCode',)
    list_filter = ('companyCode',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 



class SimulationBenefitAdmin(admin.ModelAdmin):
    list_display = ('companyCode',)
    readonly_fields = ('companyCode',) 
    search_fields = ('companyCode',)
    list_filter = ('companyCode',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 





admin.site.register(SimulationBenefit,SimulationBenefitAdmin)
admin.site.register(SummedActualCost,SummedActualCostAdmin)
