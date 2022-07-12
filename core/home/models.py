from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class MainPageStatisticNumber(models.Model):
    number = models.IntegerField(null=True, blank=True, verbose_name = "Значение")
    description = models.TextField(null=True, blank=True, verbose_name = "Описание")

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"
        verbose_name = "число"


class KeyPublications(models.Model):
    title = models.TextField(null=True, blank=True, verbose_name = "Заголовок")
    authors = models.TextField(null=True, blank=True, verbose_name = "Авторы")
    journal = models.TextField(null=True, blank=True, verbose_name = "Журнал")
    publicationUrl = models.URLField(max_length=250, verbose_name = "Ссылка")
    image = models.ImageField(upload_to="media/keypublications", null=True, blank=True, verbose_name = "Афиша")

    class Meta:
        verbose_name_plural = "Основные публикации"
        verbose_name = "публикацию"


class FamousGraduates(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name = "Имя")
    shortDescription = models.TextField(null=True, blank=True, verbose_name = "Краткое описание")
    photo = models.ImageField(upload_to="media/famousGraduates", null=True, blank=True, verbose_name = "Фото")
    briefBioInfo = RichTextField(null=True, blank=True, verbose_name = "Биография")
    typeOfProfActivity = RichTextField(null=True, blank=True, verbose_name = "Область науки")
    periodOfStudy = models.TextField(null=True, blank=True, verbose_name = "Период обучения")
    facultyAndSpeciality = models.TextField(null=True, blank=True, verbose_name = "Факультет и специальность")
    professionalAchievements = RichTextField(null=True, blank=True, verbose_name = "Достижения")
    slug = models.SlugField(max_length=250, unique=True, verbose_name = "Слаг")

    class Meta:
        verbose_name_plural = "Известные выпускники"
        verbose_name = "выпускника"

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = "Афиша"
    admin_photo.allow_tags = True
