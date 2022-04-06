from modeltranslation.translator import register, TranslationOptions
from .models import MainPageStatisticNumber, FamousGraduates


@register(MainPageStatisticNumber)
class NumbersTranslationOptions(TranslationOptions):
    fields = ("description",)


@register(FamousGraduates)
class GraduatesTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "shortDescription",
        "briefBioInfo",
        "typeOfProfActivity",
        "facultyAndSpeciality",
        "professionalAchievements",
    )
