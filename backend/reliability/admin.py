from django.contrib import admin
from .models import Reliability,TroubleHistory,FailurePredictionPoint



class ReliabilityAdmin(admin.ModelAdmin):
    list_display = (
        'companyCode', 'ceListNo', 'plant', 'equipment', 'machineName', 'maintenanceTitle', 
        'mttr', 'mtbf', 'mttf', 'totalOperatingTime', 'failureCount', 'failureDate'
    )
    search_fields = ('equipment__name', 'machineName__name', 'plant')
    list_filter = ('companyCode', 'ceListNo', 'plant', 'maintenanceMethod', 'failureType', 'operationalCondition', 'PMType')
    ordering = ('-mttr',)
    save_on_top = True
    list_per_page = 50

    # 補足説明用フィールドも表示できるようにします
    fieldsets = (
        (None, {
            'fields': (
                'companyCode', 'ceListNo', 'plant', 'equipment', 'machineName', 'maintenanceTitle',
                'mttr', 'mtbf', 'mttf', 'totalOperatingTime', 'failureCount', 'failureDate',
                'failureType', 'failureTypeDetail', 'operationalCondition', 'operationalConditionDetail',
                'PMType', 'maintenanceMethod', 'maintenanceMethodDetail', 'failureMode', 'failureModeDetail',
                'failureCause', 'failureCauseDetail', 'remark', 'record_date'
            )
        }),
    )



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