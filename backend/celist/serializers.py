from rest_framework import serializers
from django.db.models import Max
from .models import CeList,CompanyCode




class CeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeList
        fields = ["companyCode","companyName","plant","ceListNo","equipment","machineName"]

class CompanyCodeCeListSerializer(serializers.ModelSerializer):
    ceList = CeListSerializer(many=True, read_only=True, source='ceList_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'ceList']


