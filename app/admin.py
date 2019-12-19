from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','eaddr','esalary']

admin.site.register(Employee,EmployeeAdmin)
