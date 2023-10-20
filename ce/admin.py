from django.contrib import admin
from .models import CeList

'''修正必要
class CeListModelAdmin(admin.ModelAdmin):
    list_display = ('status', 'bkg_no', 'flag','created_at')
    ordering = ('-created_at',)
'''


admin.site.register(CeList,'''CeListModelAdmin''')