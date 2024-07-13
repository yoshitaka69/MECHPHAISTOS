from django.contrib import admin
from .models import TroubleHistory


class TroubleHistoryAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause')
    search_fields = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause')
    list_filter = ('companyCode', 'ceListNo', 'equipment', 'machineName', 'date', 'pmType', 'failureContent', 'failureType', 'repairMethod', 'repairCost', 'rootCause')
    ordering = ('companyCode',)
    save_on_top = True
    list_per_page = 50

admin.site.register(TroubleHistory, TroubleHistoryAdmin)