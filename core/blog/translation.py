from modeltranslation.translator import register, TranslationOptions
from .models import Post, NoteInMedia


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ("title", "body")


@register(NoteInMedia)
class NoteInMediaTranslationOptions(TranslationOptions):
    fields = ("title", "body")
