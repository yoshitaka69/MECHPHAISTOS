from django.contrib import admin
from .models import Reliability,TroubleHistory,FailurePredictionPoint



class ReliabilityAdmin(admin.ModelAdmin):
    list_display = (
        'companyCode', 'ceListNo', 'plant', 'equipment', 'machineName',
        'failureType', 'operationalCondition', 'PMType', 'maintenanceMethod', 
        'maintenanceFrequency', 'failureMode', 'failureCause', 'componentCondition', 
        'mttr', 'mtbf', 'mttf', 'totalOperatingTime', 'failureCount', 'failureDate', 'record_date'
    )
    list_filter = ('failureType', 'operationalCondition', 'PMType', 'failureMode', 'failureCause')
    search_fields = ('plant', 'machineName__name', )  # 外部キーのフィールドを指定する場合は__で連結
    ordering = ['-mttr']  # `Meta`の設定を反映させる
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