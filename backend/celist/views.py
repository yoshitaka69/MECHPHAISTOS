from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


from .models import Ce,SpareParts,Task,Company
from .serializers import CeSerializer,SparePartsSerializer,TaskSerializer,CompanyCeSerializer


#Critical equipment list
class CeViewSet(viewsets.ModelViewSet):
    queryset = Ce.objects.all()
    serializer_class = CeSerializer

class CeByCompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CeSerializer

    def get_queryset(self):
        companyCode_slug = self.kwargs['companyCode_slug']
        return Ce.objects.filter(companyCode__slug=companyCode_slug)

@api_view(['GET'])
def company_ce_list(request):
    companies = Company.objects.all()
    serializer = CompanyCeSerializer(companies, many=True)
    return Response(serializer.data)


class SparePartsViewSet(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        spareParts = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(spareParts)
        return Response(serializer.data)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(task)
        return Response(serializer.data)