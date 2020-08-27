from django.contrib import admin
from .models import Advertisement
from .models import QuantumCourse
from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "body", "publish")



@admin.register(QuantumCourse)
class QuantumCourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ('advertisement',)
