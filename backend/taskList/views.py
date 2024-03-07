from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


from .models import TaskList,Company
from .serializers import TaskSerializer,CompanyTaskSerializer


#Critical equipment list
class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer

class TaskListByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return TaskList.objects.filter(companyCode__slug=companyCode_slug)

@api_view(['GET'])
def company_task_list(request):
    companies = Company.objects.all()
    serializer = CompanyTaskSerializer(companies, many=True)
    return Response(serializer.data)