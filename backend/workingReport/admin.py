from django.contrib import admin
from .models import EquipmentSpecification,InspectionForm

@admin.register(EquipmentSpecification)
class EquipmentSpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'model_number', 'purchase_date')
    search_fields = ('name', 'manufacturer', 'model_number')



@admin.register(InspectionForm)
class InspectionFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'extracted_text')  # 管理画面に表示するフィールドを指定
    search_fields = ('name', 'extracted_text')  # 検索可能なフィールドを指定
    list_filter = ('uploaded_at',)  # フィルタ可能なフィールドを指定