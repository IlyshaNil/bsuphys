from modeltranslation.translator import register, TranslationOptions
from .models import Staff_unit


@register(Staff_unit)
class PostTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'academic_rank', 'description', 'address')