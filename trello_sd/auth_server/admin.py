from django.contrib import admin

from auth_server.models import Employee, SubDivision


class EmployeeAdmin(admin.ModelAdmin):
    pass


class SubDivisionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(SubDivision, SubDivisionAdmin)
