from django.contrib import admin
from .models import CustomUser, Company, UserInfo, Payment

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'date_joined', 'company', 'user_info', 'payment')
    search_fields = ('email', 'company__companyName', 'user_info__userName', 'payment__companyName')
    ordering = ('email',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyListNo', 'companyName', 'country', 'zipCode', 'accountType', 'createdDay', 'updateDay')
    search_fields = ('companyListNo', 'companyName')
    ordering = ('companyName',)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('userName', 'firstName', 'familyName', 'email', 'phoneNumber', 'createdDay', 'updateDay')
    search_fields = ('userName', 'email')
    ordering = ('userName',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('companyCode', 'companyName', 'country', 'zipCode', 'accountType', 'createdDay', 'updateDay')
    search_fields = ('companyCode', 'companyName')
    ordering = ('companyName',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Payment, PaymentAdmin)
