from modeltranslation.translator import register, TranslationOptions
from .models import MainPageStatisticNumber


@register(MainPageStatisticNumber)
class NumbersTranslationOptions(TranslationOptions):
    fields = ('description')