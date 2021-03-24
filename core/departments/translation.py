from modeltranslation.translator import register, TranslationOptions
from .models import Department


@register(Department)
class PostTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'description', 'thesis_themes', 'science_directions', 'publications', 'courses')
