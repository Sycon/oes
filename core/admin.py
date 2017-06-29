from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class FlatPageAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets+(
        ('Advanced options', {
#            'classes': ('collapse',),
            'fields': ('bio', 'location'),
        }),
    )


# Register your models here.
admin.site.register(models.User, FlatPageAdmin)
admin.site.register(models.Adminlogin)
admin.site.register(models.Question)
admin.site.register(models.School)
admin.site.register(models.Student)
admin.site.register(models.Studentquestion)
admin.site.register(models.Studenttest)
admin.site.register(models.Subject)
admin.site.register(models.Test)
admin.site.register(models.Testconductor)
