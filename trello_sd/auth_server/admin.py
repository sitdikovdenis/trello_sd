from django.contrib import admin

from auth_server.models import Employee, SubDivision, MirricoManagementUser2, RegisterVerificationCode


class EmployeeAdmin(admin.ModelAdmin):
    pass


class SubDivisionAdmin(admin.ModelAdmin):
    pass


class MirricoManagementUser2Admin(admin.ModelAdmin):
    pass


class RegisterVerificationCodesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(SubDivision, SubDivisionAdmin)
admin.site.register(MirricoManagementUser2, MirricoManagementUser2Admin)
admin.site.register(RegisterVerificationCode, RegisterVerificationCodesAdmin)
