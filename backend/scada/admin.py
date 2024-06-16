from django.contrib import admin
from .models import CanvasState

@admin.register(CanvasState)
class CanvasStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    readonly_fields = ('created_at',)
