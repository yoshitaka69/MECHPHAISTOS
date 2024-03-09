from django.contrib import admin
from .models import CustomUser, Company, Payment

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'firstName', 'familyName', 'email', 'phoneNumber', 'is_active', 'is_staff', 'companyName', 'payment','createdDay', 'updateDay')
    search_fields = ('userName', 'email','company''payment', )
    list_filter = ('userName',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('userName', )

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyListNo', 'companyName', 'country', 'zipCode', 'payment', 'createdDay', 'updateDay')
    search_fields = ('companyListNo', 'companyName')
    list_filter = ('companyCode',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyName',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('paymentType','description',)
    search_fields = ('paymentType','description',)
    list_filter = ('paymentType','description',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('paymentType',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Payment, PaymentAdmin)
