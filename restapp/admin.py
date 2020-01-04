from django.contrib import admin
from .models import EmployeeDetails

# Register your models here.
class EmployeeDetailsAdmin(admin.ModelAdmin):
	list_display = ('e_name','e_email','e_number')

admin.site.register(EmployeeDetails,EmployeeDetailsAdmin)