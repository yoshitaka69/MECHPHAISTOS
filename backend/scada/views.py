from django.shortcuts import render
from rest_framework import generics
from .models import CanvasState
from .serializers import CanvasStateSerializer

def index(request):
    return render(request, 'scada/index.html')

class CanvasStateListCreate(generics.ListCreateAPIView):
    queryset = CanvasState.objects.all()
    serializer_class = CanvasStateSerializer
