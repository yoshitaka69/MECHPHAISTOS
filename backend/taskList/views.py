from rest_framework import viewsets

from .models import TaskList,CompanyCode
from .serializers import TaskListSerializer,CompanyTaskListSerializer

#Critical equipment list
class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class CompanyCodeTaskListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyTaskListSerializer

    def get_queryset(self):
        return CompanyCode.objects.prefetch_related('taskList_companyCode').all()