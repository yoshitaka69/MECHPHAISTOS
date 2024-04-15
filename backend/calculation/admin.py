from django.contrib import admin
from .models import (CalTablePlannedPM02,CalTableActualPM02,
                     CalTablePlannedPM03,CalTableActualPM03,
                     CalTableActualPM04,
                     CalTablePlannedPM05,CalTableActualPM05,
                     SummedPlannedCost,SummedActualCost)



# Register your models here.
class CalTablePlannedPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTabelActualPM02Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTablePlannedPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 



class CalTabelActualPM03Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTabelActualPM04Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTablePlannedPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 


class CalTabelActualPM05Admin(admin.ModelAdmin):
    list_display = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    search_fields = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    list_filter = ('companyCode','companyName','plant','no1HighCost','no2HighCost','no3HighCost','no4HighCost','no5HighCost','no1LowCost','averageCost',)
    ordering = ('plant',)
    save_on_top = True

    list_per_page = 50 




class SummedPlannedCostAdmin(admin.ModelAdmin):
    list_display = ('companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalPlannedPM02','totalPlannedPM03','totalPlannedPM04','totalPlannedPM05','totalPlannedCost',)
    search_fields = ('companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalPlannedPM02','totalPlannedPM03','totalPlannedPM04','totalPlannedPM05','totalPlannedCost',)
    list_filter = ('companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalPlannedPM02','totalPlannedPM03','totalPlannedPM04','totalPlannedPM05','totalPlannedCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 



class SummedActualCostAdmin(admin.ModelAdmin):
    list_display = ('companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalActualPM02','totalActualPM03','totalActualPM04','totalActualPM05','totalActualCost',)
    search_fields = ('companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalActualPM02','totalActualPM03','totalActualPM04','totalActualPM05','totalActualCost',)
    list_filter = ('companyCode','plant','year','sumJan','sumFeb','sumMar','sumApr','sumMay','sumJun','sumJul','sumAug','sumSep','sumOct','sumNov','sumDec','sumCommitment','totalActualPM02','totalActualPM03','totalActualPM04','totalActualPM05','totalActualCost',)
    ordering = ('companyCode',)
    save_on_top = True

    list_per_page = 50 






admin.site.register(CalTablePlannedPM02,CalTablePlannedPM02Admin)
admin.site.register(CalTableActualPM02,CalTabelActualPM02Admin)
admin.site.register(CalTablePlannedPM03,CalTablePlannedPM03Admin)
admin.site.register(CalTableActualPM03,CalTabelActualPM03Admin)
admin.site.register(CalTableActualPM04,CalTabelActualPM04Admin)
admin.site.register(CalTablePlannedPM05,CalTablePlannedPM05Admin)
admin.site.register(CalTableActualPM05,CalTabelActualPM05Admin)

admin.site.register(SummedPlannedCost,SummedPlannedCostAdmin)
admin.site.register(SummedActualCost,SummedActualCostAdmin)