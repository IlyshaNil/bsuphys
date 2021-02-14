from django.contrib import admin
from .models import MainPageStatisticNumber, KeyPublications, FamousGraduates
from modeltranslation.admin import TranslationAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = "Сайт Физического факультета БГУ"

@admin.register(MainPageStatisticNumber)
class MainPageStaticNumbersAdmin(TranslationAdmin):
    list_display = ["number", "description"]

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"



@admin.register(KeyPublications)
class KeyPublications(admin.ModelAdmin):
    list_display = ["title", "authors", "journal"]


@admin.register(FamousGraduates)
class FamousGraduatesAdmin(TranslationAdmin):
    list_display = ["name", "shortDescription", "facultyAndSpeciality"]
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"
