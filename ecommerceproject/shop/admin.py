from django.contrib import admin
from . models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['Name', 'slug']
    prepopulated_fields = {'slug': ('Name',)}
admin.site.register(Category,CategoryAdmin)

class PorductAdmin(admin.ModelAdmin):
    #list_display = ['Name', 'Price', 'Stock', 'Available', 'created', 'Updated']
    #list_editable = ['Price', 'Stock', 'Available']
    prepopulated_fields = {'slug': ('Name',)}
    list_per_page = 20
admin.site.register(Product,PorductAdmin)