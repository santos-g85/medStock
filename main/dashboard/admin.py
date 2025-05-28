from django.contrib import admin
from .models import Medicine,Supplier
# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name','description','quantity_in_stock','price') 
    search_fields = ('name','quantity_in_stock')  
    list_filter = ('name', 'quantity_in_stock')  
    list_per_page = 10
    list_display_links = ('name', 'description')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','contact','email','address') 
    search_fields = ('name','contact')  
    list_filter = ('name', 'contact','email')  
    list_per_page = 10
    list_display_links = ('name', 'contact')