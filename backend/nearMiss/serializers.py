from rest_framework import serializers
from .models import NearMiss, Company

class NearMissSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearMiss
        fields = '__all__'

class CompanyNearMissSerializer(serializers.ModelSerializer):
    nearMissList = NearMissSerializer(many=True, read_only=True, source='nearmiss_set')

    class Meta:
        model = Company
        fields = ['companyCode', 'nearMissList']