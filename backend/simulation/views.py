from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import No1Simulation, No2Simulation, No3Simulation
from .serializers import (
    CompanyCodeNo1SimulationSerializer,
    CompanyCodeNo2SimulationSerializer,
    CompanyCodeNo3SimulationSerializer,
    No1SimulationSerializer,
    No2SimulationSerializer,
    No3SimulationSerializer
)
from accounts.models import CompanyCode





#------------------------------------------------------------
# No1Simulationの新規作成、取得、更新、削除のためのビュー
class No1SimulationAPIView(viewsets.ModelViewSet):

    def post(self, request, *args, **kwargs):
        serializer = No1SimulationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        simulations = No1Simulation.objects.all()
        serializer = No1SimulationSerializer(simulations, many=True)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            simulation = No1Simulation.objects.get(pk=pk)
        except No1Simulation.DoesNotExist:
            return Response({'error': 'Simulation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = No1SimulationSerializer(simulation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            simulation = No1Simulation.objects.get(pk=pk)
        except No1Simulation.DoesNotExist:
            return Response({'error': 'Simulation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        simulation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CompanyCodeに関連するNo1Simulationリストを取得
class CompanyCodeNo1SimulationListView(viewsets.ModelViewSet):
    serializer_class = CompanyCodeNo1SimulationSerializer

    def get_queryset(self):
        company_code = self.kwargs['company_code']
        return CompanyCode.objects.filter(companyCode=company_code)

#------------------------------------------------------------




#------------------------------------------------------------

# No2Simulationの新規作成、取得、更新、削除のためのビュー
class No2SimulationAPIView(viewsets.ModelViewSet):

    def post(self, request, *args, **kwargs):
        serializer = No2SimulationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        simulations = No2Simulation.objects.all()
        serializer = No2SimulationSerializer(simulations, many=True)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            simulation = No2Simulation.objects.get(pk=pk)
        except No2Simulation.DoesNotExist:
            return Response({'error': 'Simulation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = No2SimulationSerializer(simulation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            simulation = No2Simulation.objects.get(pk=pk)
        except No2Simulation.DoesNotExist:
            return Response({'error': 'Simulation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        simulation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CompanyCodeに関連するNo2Simulationリストを取得
class CompanyCodeNo2SimulationListView(viewsets.ModelViewSet):
    serializer_class = CompanyCodeNo2SimulationSerializer

    def get_queryset(self):
        company_code = self.kwargs['company_code']
        return CompanyCode.objects.filter(companyCode=company_code)

#------------------------------------------------------------




#------------------------------------------------------------

# No3Simulationの新規作成、取得、更新、削除のためのビュー
class No3SimulationAPIView(viewsets.ModelViewSet):

    def post(self, request, *args, **kwargs):
        serializer = No3SimulationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        simulations = No3Simulation.objects.all()
        serializer = No3SimulationSerializer(simulations, many=True)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            simulation = No3Simulation.objects.get(pk=pk)
        except No3Simulation.DoesNotExist:
            return Response({'error': 'Simulation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = No3SimulationSerializer(simulation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            simulation = No3Simulation.objects.get(pk=pk)
        except No3Simulation.DoesNotExist:
            return Response({'error': 'Simulation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        simulation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CompanyCodeに関連するNo3Simulationリストを取得
class CompanyCodeNo3SimulationListView(viewsets.ModelViewSet):
    serializer_class = CompanyCodeNo3SimulationSerializer

    def get_queryset(self):
        company_code = self.kwargs['company_code']
        return CompanyCode.objects.filter(companyCode=company_code)
    
#------------------------------------------------------------