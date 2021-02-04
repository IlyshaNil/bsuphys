from django.db import models

# Create your models here.

class MainPageStatisticNumber(models.Model):
    number = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"


class KeyPublications(models.Model):
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    journal= models.TextField(null=True, blank=True)
    publicationUrl = models.URLField(max_length=250)
    image = models.ImageField(upload_to="media/keypublications", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Основные публикации"
        