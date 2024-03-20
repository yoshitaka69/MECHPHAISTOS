from django.shortcuts import render
from rest_framework import viewsets

from .models import MasterDataTable
from taskList.models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05
from spareParts.models import BomList
from accounts.models import CompanyCode
from .serializers import (
    TaskListPM02MasterSerializer, TaskListPM03MasterSerializer, 
    TaskListPM04MasterSerializer, TaskListPM05MasterSerializer, 
    BomListMasterSerializer, MasterDataTableSerializer, CompanyCodeMDTSerializer
)


class TaskListPM02MasterViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM02.objects.all()
    serializer_class = TaskListPM02MasterSerializer

class TaskListPM03MasterViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM03.objects.all()
    serializer_class = TaskListPM03MasterSerializer

class TaskListPM04MasterViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM04.objects.all()
    serializer_class = TaskListPM04MasterSerializer

class TaskListPM05MasterViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM05.objects.all()
    serializer_class = TaskListPM05MasterSerializer

class BomListMasterViewSet(viewsets.ModelViewSet):
    queryset = BomList.objects.all()
    serializer_class = BomListMasterSerializer
    
class MasterDataTableViewSet(viewsets.ModelViewSet):
    queryset = MasterDataTable.objects.all()
    serializer_class = MasterDataTableSerializer

class CompanyCodeMDTViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyCodeMDTSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('masterDataTable_companyCode').all()#ここでのrelatedNameの間違いは要注意