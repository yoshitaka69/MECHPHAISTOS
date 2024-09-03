# scada/serializers.py
from rest_framework import serializers
from .models import CanvasState

class CanvasStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanvasState
        fields = ['id', 'data', 'created_at']
