from rest_framework import viewsets

from accounts.models import CompanyCode
from .models import TaskListPPM02,TaskListAPM02,TaskListPPM03,TaskListAPM03,TaskListPPM04,TaskListPPM05,TaskListAPM05,TypicalTaskList,TaskList
from .serializers import (TaskListPPM02Serializer,CompanyTaskListPPM02Serializer,
                          TaskListAPM02Serializer,CompanyTaskListAPM02Serializer,

                          TaskListPPM03Serializer,CompanyTaskListPPM03Serializer,
                          TaskListAPM03Serializer,CompanyTaskListAPM03Serializer,

                          TaskListPM04Serializer,CompanyTaskListPM04Serializer,

                          TaskListPPM05Serializer,CompanyTaskListPPM05Serializer,
                          TaskListAPM05Serializer,CompanyTaskListAPM05Serializer,

                          TypicalTaskListSerializer,CompanyTypicalTaskListSerializer,
                          TaskListSerializer,CompanyTaskListSerializer)



#TasKListPPM02
class TaskListPPM02ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPPM02.objects.all()
    serializer_class = TaskListPPM02Serializer

class CompanyCodeTaskListPPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPPM02_companyCode').all()
    


#TaskListAPM02
class TaskListAPM02ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM02.objects.all()
    serializer_class = TaskListAPM02Serializer

class CompanyCodeTaskListAPM02ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM02Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM02_companyCode').all()





#TaskListPPM03
class TaskListPPM03ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPPM03.objects.all()
    serializer_class = TaskListPPM03Serializer

class CompanyCodeTaskListPPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPPM03_companyCode').all()



#TaskListAPM03
class TaskListAPM03ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM03.objects.all()
    serializer_class = TaskListAPM03Serializer

class CompanyCodeTaskListAPM03ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM03Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM03_companyCode').all()




#TaskListAPM04
class TaskListAPM04ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM04.objects.all()
    serializer_class = TaskListAPM04Serializer

class CompanyCodeTaskListAPM04ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM04Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM04_companyCode').all()




#TaskListPPM05
class TaskListPPM05ViewSet(viewsets.ModelViewSet):
    queryset = TaskListPPM05.objects.all()
    serializer_class = TaskListPPM05Serializer

class CompanyCodeTaskListPPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListPPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListPPM05_companyCode').all()



#TaskListAPM05
class TaskListAPM05ViewSet(viewsets.ModelViewSet):
    queryset = TaskListAPM05.objects.all()
    serializer_class = TaskListAPM05Serializer

class CompanyCodeTaskListAPM05ViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyTaskListAPM05Serializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskListAPM05_companyCode').all()





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
