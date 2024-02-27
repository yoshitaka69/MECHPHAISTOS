from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request


from .models import Ce,SpareParts,Task
from .serializers import CeSerializer,SparePartsSerializer,TaskSerializer

class CeViewSet(viewsets.ModelViewSet):
    queryset = Ce.objects.all()
    serializer_class = CeSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        ce = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(ce)
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