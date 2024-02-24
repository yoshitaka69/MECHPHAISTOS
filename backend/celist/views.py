from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CeList,SparePartsList,TaskList
from .serializers import CeListSerializer,SparePartsListSerializer,TaskListSerializer


class CeListView(APIView):
    def get(self, request, format=None):
        ceList = CeList.objects.all()[0:4] 
        serializer = CeListSerializer(ceList, many=True)
        return Response(serializer.data)

class SparePartsListView(APIView):
    def get(self, request, format=None):
        sparePartsList = SparePartsList.objects.all()[0:4] 
        serializer = SparePartsListSerializer(sparePartsList, many=True)
        return Response(serializer.data)
    
class TaskListView(APIView):
    def get(self, request, format=None):
        taskList = TaskList.objects.all()[0:4] 
        serializer = TaskListSerializer(taskList, many=True)
        return Response(serializer.data)