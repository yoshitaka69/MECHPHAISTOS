from django.contrib import admin
from .models import Reliability,TroubleHistory,FailurePredictionPoint



class ReliabilityAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'mttr', 'mtbf', 'mttf', 'totalOperatingTime', 'failureCount')
    search_fields = ('equipment__name', 'machineName__name')
    list_filter = ('companyCode', 'ceListNo')
    ordering = ('-mttr',)
    save_on_top = True
    list_per_page = 50



class FailurePredictionPointAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', )
    search_fields = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', )
    list_filter = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', )
    ordering = ('companyCode',)
    save_on_top = True
    list_per_page = 50


class TroubleHistoryAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause')
    search_fields = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause')
    list_filter = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause')
    ordering = ('companyCode',)
    save_on_top = True
    list_per_page = 50





admin.site.register(Reliability, ReliabilityAdmin)
admin.site.register(FailurePredictionPoint, FailurePredictionPointAdmin)
admin.site.register(TroubleHistory, TroubleHistoryAdmin)