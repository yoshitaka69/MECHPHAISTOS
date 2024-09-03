from django.db import models
from accounts.models import CompanyCode


#作業報告書
from django.db import models

class MaintenanceWorkingReport(models.Model):
    company_code = models.CharField(max_length=255)
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    equipment = models.CharField(max_length=255)
    part_name = models.CharField(max_length=255, blank=True, null=True)
    reporter = models.CharField(max_length=255)
    pm_type = models.CharField(max_length=255)
    summary_remarks = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_code} - {self.uploaded_at}"





#--------------------------------------------------------------

from django.db import models

class Specsheets(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='specsheets_companyCode', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title if self.title else "No Title"






#--------------------------------------------------------------



#点検表
class InspectionForm(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='inspection_forms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
