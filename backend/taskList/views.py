from rest_framework import viewsets

from .models import TaskListPM02,TaskListPM03,TaskListPM04,TaskListPM05,CompanyCode
from .serializers import TaskListPM02Serializer,CompanyTaskListPM02Serializer,TaskListPM03Serializer,CompanyTaskListPM03Serializer,TaskListPM04Serializer,CompanyTaskListPM04Serializer,TaskListPM05Serializer,CompanyTaskListPM05Serializer

#Critical equipment list
class TaskListPM02ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM02.objects.all()
    serializer_class = TaskListPM02Serializer

class CompanyCodeTaskListPM02ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyTaskListPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM02_companyCode').all()
    



class TaskListPM03ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM03.objects.all()
    serializer_class = TaskListPM03Serializer

class CompanyCodeTaskListPM03ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyTaskListPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM03_companyCode').all()
    



class TaskListPM04ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM04.objects.all()
    serializer_class = TaskListPM04Serializer

class CompanyCodeTaskListPM04ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyTaskListPM04Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM04_companyCode').all()




class TaskListPM05ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPM05.objects.all()
    serializer_class = TaskListPM05Serializer

class CompanyCodeTaskListPM05ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyTaskListPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPM05_companyCode').all()