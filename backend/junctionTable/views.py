from django.shortcuts import render
from rest_framework import viewsets

from .models import MasterDataTable,BomToTask,AlertSchedule
from accounts.models import CompanyCode
from .serializers import  (MasterDataTableSerializer, CompanyCodeMDTSerializer,
                        BomToTaskSerializer,CompanyCodeBomToTaskSerializer,
                        AlertScheduleSerializer,CompanyCodeAlertScheduleSerializer)


    
class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer


class CompanyCodeMDTViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyCodeMDTSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('masterDataTable_companyCode').all()#ここでのrelatedNameの間違いは要注意
