from django.contrib import admin
from django.db import models
from django.contrib import admin
from .models import Post
from django import forms
from blog.models import Post as news


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # formfield_overrides = {news.title: {"widget": forms.TextInput}}
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")
