from django.contrib import admin
from .models import Staff_unit
from django.db import models
from django import forms
from modeltranslation.admin import TranslationAdmin


@admin.register(Staff_unit)
class StaffAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "position", "specialization"]
    list_filter = ["position", "specialization", "position_var"]
    # formfield_overrides = {models.TextField: {"widget": forms.TextInput}}

    class Meta:
        verbose_name_plural = "Сотрудники"
