from django.contrib import admin
from .models import ImageAnalysis

@admin.register(ImageAnalysis)
class ImageAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'label', 'predicted_label', 'created_at')
    search_fields = ('id', 'label', 'predicted_label')
    list_filter = ('created_at',)