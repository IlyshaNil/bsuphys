from django.contrib import admin
from .models import Post
from .models import NoteInMedia
from modeltranslation.admin import TranslationAdmin
from django.contrib.admin import SimpleListFilter


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ("title", "slug", "author", "publish", "status", "admin_photo")
    list_filter = (PostFilter, )
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")



@admin.register(NoteInMedia)
class NoteInMediaAdmin(TranslationAdmin):
    list_display = ("title", "body", "status", "admin_photo")
    prepopulated_fields = {"slug": ("title",)}


class PostFilter(SimpleListFilter):
    title = 'Status' # or use _('country') for translated title
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ("draft", "Draft"),
            ("published", "Published"),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'draft':
            return queryset.filter(status__status='draft')
        if self.value() == 'published':
            return queryset.filter(status__status='published')

# class PostFilter(SimpleListFilter):
#     title = 'Status' # or use _('country') for translated title
#     parameter_name = 'status'

#     def lookups(self, request, model_admin):
#         posts = set([c.status for c in Post.model.objects.all()])
#         return [(c.id, c.title) for c in countries] + [
#           ('draft', 'Draft - all')]

#     def queryset(self, request, queryset):
#         if self.value() == 'draft':
#             return queryset.filter(status__status='draft')
#         if self.value():
#             return queryset.filter(status__id__exact=self.value())