from rest_framework import serializers
from .models import EquipmentSpecification, InspectionForm

class EquipmentSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentSpecification
        fields = '__all__'


class InspectionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionForm
        fields = '__all__'