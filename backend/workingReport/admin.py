from django.contrib import admin
from .models import InspectionForm

from django.contrib import admin
from .models import MaintenanceWorkingReport

@admin.register(MaintenanceWorkingReport)
class MaintenanceWorkingReportAdmin(admin.ModelAdmin):
    list_display = ('company_code', 'task_name', 'start_date', 'end_date', 'reporter', 'uploaded_at')
    search_fields = ('company_code', 'task_name', 'reporter', 'equipment', 'part_name')
    list_filter = ('company_code', 'start_date', 'end_date', 'uploaded_at')
    ordering = ('-uploaded_at',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # 編集時は以下のフィールドを読み取り専用にする
            return ['company_code', 'pdf_file', 'uploaded_at']
        else:  # 新規作成時はすべてのフィールドを編集可能にする
            return []



from django.contrib import admin
from .models import Specsheets


@admin.register(Specsheets)
class SpecsheetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)



@admin.register(InspectionForm)
class InspectionFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at', 'extracted_text')  # 管理画面に表示するフィールドを指定
    search_fields = ('name', 'extracted_text')  # 検索可能なフィールドを指定
    list_filter = ('uploaded_at',)  # フィルタ可能なフィールドを指定