from rest_framework import generics
from ce.models import CeList
from ce.API.serializers import CeSerializer



class ListView(generics.ListCreateAPIView):
    queryset = CeList.objects.all().order_by('-id')
    serializer_class = CeSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CeList.objects.all()
    serializer_class = CeSerializer

    