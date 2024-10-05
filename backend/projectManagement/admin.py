from django.contrib import admin
from .models import ProjectManagement

@admin.register(ProjectManagement)
class ProjectManagementAdmin(admin.ModelAdmin):
    list_display = ('projectName', 'name', 'companyCode', 'uploadedBy', 'registrationDate')  # 管理画面のリスト表示
    search_fields = ('projectName', 'name', 'uploadedBy')  # 検索フィールド
    list_filter = ('categories', 'registrationDate', 'companyCode')  # フィルタ機能
    date_hierarchy = 'registrationDate'  # 登録日でナビゲーション
    ordering = ('-registrationDate',)  # 登録日の降順で並べ替え
    fieldsets = (
        (None, {
            'fields': ('companyCode', 'projectName', 'name', 'file', 'categories', 'uploadedBy', 'registrationDate', 'tag')
        }),
    )
