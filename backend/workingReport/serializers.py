from rest_framework import serializers
from .models import InspectionForm

from rest_framework import serializers
from .models import MaintenanceWorkingReport

class MaintenanceWorkingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceWorkingReport
        fields = [
            'company_code', 
            'task_name', 
            'description', 
            'start_date', 
            'end_date', 
            'equipment', 
            'part_name', 
            'reporter', 
            'pm_type', 
            'images', 
            'additional_notes', 
            'summary_remarks', 
            'pdf_file', 
            'uploaded_at'
        ]




#--------------------------------------------------------------

from rest_framework import serializers
from .models import Specsheets

class SpecsheetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specsheets
        fields = '__all__'





#--------------------------------------------------------------





class InspectionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionForm
        fields = '__all__'