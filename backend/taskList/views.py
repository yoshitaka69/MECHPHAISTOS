from rest_framework import viewsets

from accounts.models import CompanyCode
from .models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05,TypicalTaskList,TaskList
from .serializers import (TaskListPM02Serializer,CompanyTaskListPM02Serializer,
                          TaskListPM03Serializer,CompanyTaskListPM03Serializer,
                          TaskListPM04Serializer,CompanyTaskListPM04Serializer,
                          TaskListPM05Serializer,CompanyTaskListPM05Serializer,
                          TypicalTaskListSerializer,CompanyTypicalTaskListSerializer,
                          TaskListSerializer,CompanyTaskListSerializer)

#Critical equipment list
class TaskListPM02ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM02.objects.all()
    serializer_class = TaskListPM02Serializer

class CompanyCodeTaskListPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM02_companyCode').all()
    



class TaskListPM03ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM03.objects.all()
    serializer_class = TaskListPM03Serializer

class CompanyCodeTaskListPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM03_companyCode').all()
    



class TaskListPM04ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM04.objects.all()
    serializer_class = TaskListPM04Serializer

class CompanyCodeTaskListPM04ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPM04Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM04_companyCode').all()




class TaskListPM05ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM05.objects.all()
    serializer_class = TaskListPM05Serializer

class CompanyCodeTaskListPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM05_companyCode').all()
    



#TypicalTaskList
class TypicalTaskListViewSet(viewsets.ModelViewSet):
    queryset = TypicalTaskList.objects.all()
    serializer_class = TypicalTaskListSerializer

class CompanyCodeTypicalTaskListViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTypicalTaskListSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('typicalTaskList_companyCode').all()
    



#TaskList
class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class CompanyCodeTaskListViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskList_companyCode').all()