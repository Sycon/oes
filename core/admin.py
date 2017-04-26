from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Adminlogin)
admin.site.register(models.Question)
admin.site.register(models.School)
admin.site.register(models.Student)
admin.site.register(models.Studentquestion)
admin.site.register(models.Studenttest)
admin.site.register(models.Subject)
admin.site.register(models.Test)
admin.site.register(models.Testconductor)
