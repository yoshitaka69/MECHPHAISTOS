from rest_framework import serializers
from .models import NearMiss, CompanyCode

class NearMissSerializer(serializers.ModelSerializer):
    dateOfOccurrence = serializers.DateField(format="%Y-%m-%d")
    createdDay = serializers.DateTimeField(format="%Y-%m-%d")
    updateDay = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = NearMiss
        fields = '__all__'

class CompanyNearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissSerializer(many=True, read_only=True, source='nearmiss_set')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'nearMissList']
