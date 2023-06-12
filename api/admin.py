from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Staff


# Register your models here.
@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'phone', 'address', 'position', 'experience', 'work_start_time', 'work_end_time')
    list_filter = ('position',)
    search_fields = ('last_name', 'first_name', 'middle_name', 'phone')
    ordering = ('last_name', 'first_name')     