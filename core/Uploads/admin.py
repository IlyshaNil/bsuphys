from django.contrib import admin
from .models import Uploads


@admin.register(Uploads)
class UploadsAdmin(admin.ModelAdmin):
    list_display = ["title", "file", "created"]
    list_filter = ["created"]
