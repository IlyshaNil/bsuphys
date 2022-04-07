from django.contrib import admin
from .models import Post
from .models import NoteInMedia
from modeltranslation.admin import TranslationAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ("title", "slug", "author", "publish", "status", "admin_photo")
    list_filter = ("publish", "status")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")


@admin.register(NoteInMedia)
class NoteInMediaAdmin(TranslationAdmin):
    list_display = ("title", "body", "status", "admin_photo")
    prepopulated_fields = {"slug": ("title",)}
