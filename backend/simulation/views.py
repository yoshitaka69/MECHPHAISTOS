from rest_framework import viewsets
from .models import BaseSimulation
from .serializers import BaseSimulationSerializer
from .models import No1Simulation
from .serializers import No1SimulationSerializer

class BaseSimulationViewSet(viewsets.ModelViewSet):
    queryset = BaseSimulation.objects.all()
    serializer_class = BaseSimulationSerializer


from rest_framework import viewsets
from .models import No1Simulation
from .serializers import No1SimulationSerializer

class No1SimulationViewSet(viewsets.ModelViewSet):
    queryset = No1Simulation.objects.all()
    serializer_class = No1SimulationSerializer


from rest_framework import viewsets
from .models import No2Simulation
from .serializers import No2SimulationSerializer

class No2SimulationViewSet(viewsets.ModelViewSet):
    queryset = No2Simulation.objects.all()
    serializer_class = No2SimulationSerializer


from rest_framework import viewsets
from .models import No3Simulation
from .serializers import No3SimulationSerializer

class No3SimulationViewSet(viewsets.ModelViewSet):
    queryset = No3Simulation.objects.all()
    serializer_class = No3SimulationSerializer