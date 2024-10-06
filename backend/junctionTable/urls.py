from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (MasterDataTableViewSet,CompanyCodeMDTViewSet,
                    BomAndTaskViewSet,CompanyCodeBomAndTaskViewSet,
                    CeListAndTaskViewSet,CompanyCodeCeListAndTaskViewSet,
                    BadActorManagementViewSet,CompanyCodeBadActorViewSet,
                    EventYearPPMViewSet,CompanyCodeEventYearPPMViewSet,
                    GapOfRepairingCostViewSet,CompanyCodeGapOfRepairingCostViewSet,
                    ScheduleForGanttViewSet,CompanyCodeScheduleForGanttViewSet,
                    ScheduleForCalendarViewSet,CompanyCodeScheduleForCalendarViewSet
                    )





router = DefaultRouter()
router.register(r'masterDataTable', MasterDataTableViewSet, basename='masterDataTable')
router.register(r'masterDataTableByCompany', CompanyCodeMDTViewSet, basename='companyCode-masterDataTable')

router.register(r'bomAndTask', BomAndTaskViewSet, basename='bomAndTask')
router.register(r'bomAndTaskByCompany', CompanyCodeBomAndTaskViewSet, basename='companyCode-bomAndTask')

router.register(r'ceListAndTask', CeListAndTaskViewSet, basename='ceListAndTask')
router.register(r'ceListAndTaskByCompany', CompanyCodeCeListAndTaskViewSet, basename='companyCode-ceListAndTask')

router.register(r'badActor', BadActorManagementViewSet, basename='badActor')
router.register(r'badActorByCompany', CompanyCodeBadActorViewSet, basename='companyCode-badActor')

router.register(r'eventYearPPM', EventYearPPMViewSet, basename='eventYearPPM')
router.register(r'eventYearPPMByCompany', CompanyCodeEventYearPPMViewSet, basename='companyCode-eventYearPPM')

router.register(r'gapOfRepairingCost', GapOfRepairingCostViewSet, basename='gapOfRepairingCost')
router.register(r'gapOfRepairingCostByCompany', CompanyCodeGapOfRepairingCostViewSet, basename='companyCode-gapOfRepairingCost')


router.register(r'scheduleForGantt', ScheduleForGanttViewSet, basename='scheduleForGantt')
router.register(r'scheduleForGanttByCompany',CompanyCodeScheduleForGanttViewSet, basename='companyCode-scheduleForGantt')

router.register(r'scheduleForCalendar', ScheduleForCalendarViewSet, basename='scheduleForCalendar')
router.register(r'scheduleForCalendarByCompany',CompanyCodeScheduleForCalendarViewSet, basename='companyCode-scheduleForCalendar')


urlpatterns = [
    path('junctionTable/', include(router.urls)),

]