from rest_framework import serializers
from jobs.models import JobOffer



class JobOfferSerializser(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        fields = '__all__'