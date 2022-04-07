from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class MainPageStatisticNumber(models.Model):
    number = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"


class KeyPublications(models.Model):
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    journal = models.TextField(null=True, blank=True)
    publicationUrl = models.URLField(max_length=250)
    image = models.ImageField(upload_to="media/keypublications", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Основные публикации"


class FamousGraduates(models.Model):
    name = models.TextField(null=True, blank=True)
    shortDescription = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="media/famousGraduates", null=True, blank=True)
    briefBioInfo = RichTextField(null=True, blank=True)
    typeOfProfActivity = RichTextField(null=True, blank=True)
    periodOfStudy = models.TextField(null=True, blank=True)
    facultyAndSpeciality = models.TextField(null=True, blank=True)
    professionalAchievements = RichTextField(null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = "Известные выпускники"

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = "Афиша"
    admin_photo.allow_tags = True
