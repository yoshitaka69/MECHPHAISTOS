from rest_framework import serializers
from .models import BaseSimulation

class BaseSimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseSimulation
        fields = '__all__'


from rest_framework import serializers
from .models import No1Simulation

class No1SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = No1Simulation
        fields = '__all__'


from rest_framework import serializers
from .models import No2Simulation

class No2SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = No2Simulation
        fields = '__all__'



from rest_framework import serializers
from .models import No3Simulation

class No3SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = No3Simulation
        fields = '__all__'