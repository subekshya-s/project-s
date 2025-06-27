from django.contrib import admin
from .models import Company,Employee
from import_export import resources
from import_export.admin import ExportMixin
class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
# Register your models here.
@admin.register(Company)
class CompanyAdmin(ExportMixin, admin.ModelAdmin): #admin.ModelAdmin controls the admin interferance
      resources_class=CompanyResource
      list_display=('Company_name','location','established_year','age')
@admin.register(Employee)
class EmployeeAdmin(ExportMixin,admin.ModelAdmin):
     resources_class=EmployeeResource
     list_display=['name','position','joined_at']