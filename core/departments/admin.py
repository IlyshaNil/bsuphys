from django.contrib import admin
from django.contrib import admin
from .models import Department
from modeltranslation.admin import TranslationAdmin
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ("name", "short_description")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ('staff',)
    