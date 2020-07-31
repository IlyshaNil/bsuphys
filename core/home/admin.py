from django.contrib import admin
from .models import MainPageStatisticNumber
from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(MainPageStatisticNumber)
class MainPageStaticNumbersAdmin(TranslationAdmin):
    list_display = ["number", "description"]
    list_filter = ["number", "description"]

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"
