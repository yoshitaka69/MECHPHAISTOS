from rest_framework import generics
from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializser



class ListView(generics.ListCreateAPIView):
    queryset = JobOffer.objects.all().order_by('-id')
    serializer_class = JobOfferSerializser

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializser

    