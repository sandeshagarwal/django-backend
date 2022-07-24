from django.contrib import admin
from .models import carSales
#from import_export.admin import ImportExportActionModelAdmin
#from django.import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(carSales)
class carSalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in carSales._meta.get_fields()]

