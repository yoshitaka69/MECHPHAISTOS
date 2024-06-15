from django.db import models


#作業報告書
class EquipmentSpecification(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='equipment_images/', blank=True, null=True)
    image1_description = models.TextField(blank=True, null=True)
    image2 = models.ImageField(upload_to='equipment_images/', blank=True, null=True)
    image2_description = models.TextField(blank=True, null=True)
    image3 = models.ImageField(upload_to='equipment_images/', blank=True, null=True)
    image3_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    


#点検表
class InspectionForm(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='inspection_forms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
