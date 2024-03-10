from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request

from .models import PlannedPM02,ActualPM02,PlannedPM03,ActualPM03,ActualPM04,PlannedPM05,ActualPM05
from .serializers import PlannedPM02Serializer,ActualPM02Serializer,PlannedPM03Serializer,ActualPM03Serializer,ActualPM04Serializer,PlannedPM05Serializer,ActualPM05Serializer


class PlannedPM02ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM02.objects.all()
    serializer_class = PlannedPM02Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        plannedPM02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(plannedPM02)
        return Response(serializer.data)

class ActualPM02ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM02.objects.all()
    serializer_class = ActualPM02Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        actualPM02 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(actualPM02)
        return Response(serializer.data)


class PlannedPM03ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM03.objects.all()
    serializer_class = PlannedPM03Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        plannedPM03 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(plannedPM03)
        return Response(serializer.data)

class ActualPM03ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM03.objects.all()
    serializer_class = ActualPM03Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        actualPM03 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(actualPM03)
        return Response(serializer.data)

class ActualPM04ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM04.objects.all()
    serializer_class = ActualPM04Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        actualPM04 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(actualPM04)
        return Response(serializer.data)
    
class PlannedPM05ViewSet(viewsets.ModelViewSet):
    queryset = PlannedPM05.objects.all()
    serializer_class = PlannedPM05Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        plannedPM05 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(plannedPM05)
        return Response(serializer.data)

class ActualPM05ViewSet(viewsets.ModelViewSet):
    queryset = ActualPM05.objects.all()
    serializer_class = ActualPM05Serializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        actualPM05 = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(actualPM05)
        return Response(serializer.data)