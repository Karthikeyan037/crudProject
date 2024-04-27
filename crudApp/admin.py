from django.contrib import admin
from crudApp.models import employee

# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    emp_detail = ['first_name','last_name' , 'salary' , 'mail_add']
admin.site.register(employee , employeeAdmin)