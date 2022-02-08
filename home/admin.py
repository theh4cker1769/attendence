from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Student
# Register your models here.


admin.site.register(Student)