from django.db import models
from accounts.models import CompanyCode

class ProjectManagement(models.Model):
    companyCode = models.ForeignKey(CompanyCode, on_delete=models.CASCADE, related_name='projectManagement_companyCode', null=True, blank=True)

    projectName = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='cad_files/', null=True, blank=True)  # ファイルがnullおよび空でも許可
    categories = models.JSONField(null=True, blank=True)  # JSONFieldもnullおよび空を許可
    uploadedBy = models.CharField(max_length=255, null=True, blank=True)  # nullおよび空でも許可
    registrationDate = models.DateField(null=True, blank=True)  # nullおよび空でも許可
    tag = models.TextField(blank=True, null=True)  # nullおよび空でも許可

    def __str__(self):
        return self.name
