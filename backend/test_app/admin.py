from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'testNo')  # testNoを追加
    search_fields = ('name', 'testNo')  # 検索可能にするフィールドにtestNoを追加


from django.contrib import admin
from .models import Category, SubCategory, Item

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)