from modeltranslation.translator import register, TranslationOptions
from .models import Post, Staff_unit


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ("title", "body")


@register(Staff_unit)
class StaffTranslationOptions(TranslationOptions):
    fields = ("name", "position", "specialization", "description")
