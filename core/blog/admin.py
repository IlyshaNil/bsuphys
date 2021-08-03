from django.contrib import admin
from .models import Post
from .models import NoteInMedia
from modeltranslation.admin import TranslationAdmin
from django.contrib.admin import SimpleListFilter


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ("title", "slug", "author", "publish", "status", "admin_photo")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "publish")



@admin.register(NoteInMedia)
class NoteInMediaAdmin(TranslationAdmin):
    list_display = ("title", "body", "status", "admin_photo")
    prepopulated_fields = {"slug": ("title",)}

"""class CountryFilter(SimpleListFilter):
    title = 'status' # or use _('country') for translated title
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        countries = set([c.country for c in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in countries] + [
          ('AFRICA', 'AFRICA - ALL')]

    def queryset(self, request, queryset):
        if self.value() == 'AFRICA':
            return queryset.filter(country__continent='Africa')
        if self.value():
            return queryset.filter(country__id__exact=self.value())"""