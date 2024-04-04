from django.shortcuts import render
from rest_framework import viewsets

from .models import MasterDataTable,BomAndTask,AlertSchedule
from accounts.models import CompanyCode
from .serializers import  (MasterDataTableSerializer, CompanyCodeMDTSerializer,
                        BomAndTaskSerializer,CompanyCodeBomToTaskSerializer,
                        AlertScheduleSerializer,CompanyCodeAlertScheduleSerializer)


#MasterDataTable
class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer


class CompanyCodeMDTViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeMDTSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('masterDataTable_companyCode').all()#ここでのrelatedNameの間違いは要注意



#BomAndTask
class BomAndTaskViewSet(viewsets.ModelViewSet):
    queryset = BomAndTask.objects.all()
    serializer_class = BomAndTaskSerializer


class CompanyCodeBomAndTaskViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeBomAndTaskSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('bomAndTask_companyCode').all()#ここでのrelatedNameの間違いは要注意



#AlertSchedule
class AlertScheduleViewSet(viewsets.ModelViewSet):
    queryset = AlertSchedule.objects.all()
    serializer_class = AlertScheduleSerializer


class CompanyCodeAlertScheduleiewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeAlertScheduleSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('alertSchedule_companyCode').all()#ここでのrelatedNameの間違いは要注意
