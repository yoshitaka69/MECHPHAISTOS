from rest_framework import serializers
from .models import AlertSchedule
from accounts.models import CompanyCode,Plant




class AlertScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertSchedule
        fields = ['companyCode', 'companyName', 'plant', 'partsName', 'eventDate', 'deliveryTime', 'orderAlertDate', 'safetyRate', 'location']

    companyCode = serializers.SlugRelatedField(
        slug_field='companyCode', 
        queryset=CompanyCode.objects.all()
    )
    plant = serializers.SlugRelatedField(
        slug_field='plant', 
        queryset=Plant.objects.all()
    )


class CompanyCodeAlertScheduleSerializer(serializers.ModelSerializer):
    AlertScheduleList = AlertScheduleSerializer(many=True, source='alertSchedule_companyCode')

    class Meta:
        model = CompanyCode
        fields = ['companyCode', 'AlertScheduleList']