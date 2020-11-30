from django.contrib import admin
from .models import MainPageStatisticNumber
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = "Сайт Физического факультета БГУ"

@admin.register(MainPageStatisticNumber)
class MainPageStaticNumbersAdmin(TranslationAdmin):
    list_display = ["number", "description"]

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"
