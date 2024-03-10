from django.contrib import admin
from .models import CustomUser, Company, Payment,CompanyCode,CompanyName,AreaCode,CommunityGroup

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'firstName', 'familyName', 'email', 'phoneNumber', 'is_active', 'is_staff', 'companyName', 'payment','createdDay', 'updateDay')
    search_fields = ('userName', 'email','company''payment', )
    list_filter = ('userName',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('userName', )

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyListNo', 'companyName', 'country', 'zipCode', 'payment', 'createdDay', 'updateDay')
    search_fields = ('companyListNo', 'companyName')
    list_filter = ('companyName',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyName',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('paymentType','description',)
    search_fields = ('paymentType','description',)
    list_filter = ('paymentType','description',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('paymentType',)

class CompanyCodeAdmin(admin.ModelAdmin):
    list_display = ('companyCode','description',)
    search_fields = ('companyCode','description',)
    list_filter = ('companyCode','description',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyCode',)

class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('companyName','description',)
    search_fields = ('companyName','description',)
    list_filter = ('companyName','description',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('companyName',)

class AreaCodeAdmin(admin.ModelAdmin):
    list_display = ('country','zipCode','description',)
    search_fields = ('country','zipCode','description',)
    list_filter = ('country','zipCode','description',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('country',)

class CommunityGroupAdmin(admin.ModelAdmin):
    list_display = ('communityGroup','companyName','createdDay','updateDay',)
    search_fields = ('communityGroup','companyName','createdDay','updateDay',)
    list_filter = ('communityGroup','companyName','createdDay','updateDay',) # adminで右側にあるフィルターBOXのこと
    save_on_top = True #上部にもsaveボタンを配置
    ordering = ('communityGroup',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(CompanyCode, CompanyCodeAdmin)
admin.site.register(CompanyName, CompanyNameAdmin)
admin.site.register(AreaCode, AreaCodeAdmin)
admin.site.register(CommunityGroup, CommunityGroupAdmin)
