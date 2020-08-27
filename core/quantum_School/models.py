from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

class Advertisement(models.Model):
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class QuantumCourse(models.Model):
    name = models.TextField(null=True, blank=True)
    COURCE_CHOICES = (
        ("1", "Квант-олимпиец"),
        ("2", "Квант XI"),
        ("3", "Квант X"),
        ("4", "Квант IX"),
        ("5", "Квант-юни"),
    )
    description = models.TextField(null=True, blank=True)
    timeTable = models.ImageField(upload_to="media", null=True, blank=True)
    lectionsUrl = models.URLField(null=True, blank=True)
    consultationUrl = models.URLField(null=True, blank=True)
    taskUrl = models.URLField(null=True, blank=True)
    course = models.TextField(
        max_length=10, choices=COURCE_CHOICES, null=True, blank=True, help_text="Обязательное поле!"
    )
    advertisement = models.ManyToManyField(Advertisement)


    def __str__(self):
        return self.name


