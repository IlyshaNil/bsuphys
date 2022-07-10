from django.db import models
from Uploads.models import Uploads
from staff.staff_conf import choises
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Staff_unit(models.Model):
    name = models.TextField(verbose_name = "Имя")
    position = models.TextField(null=True, blank=True, verbose_name = "Должность")
    academic_rank = models.TextField(null=True, blank=True, verbose_name = "Степень")
    position_var = models.TextField(
        max_length=30, choices=choises.POSTION_CHOISES, null=True, blank=True, verbose_name = "Степень (знач.)"
    )
    specialization = models.TextField(
        max_length=30, choices=choises.STATUS_CHOICES, null=True, blank=True, verbose_name = "Кафедра (знач.)"
    )
    slug = models.SlugField(max_length=250, unique=True, verbose_name = "Слаг")
    image = models.ImageField(upload_to="media/staff", null=True, blank=True, verbose_name = "Фото")
    description = RichTextField(null=True, blank=True, verbose_name = "Описание")
    address = models.TextField(null=True, blank=True, verbose_name = "Адрес")
    email = models.TextField(null=True, blank=True, verbose_name = "E-mail")
    phone = models.TextField(null=True, blank=True, verbose_name = "Телефон")
    uploads = models.ForeignKey(
        Uploads, null=True, blank=True, on_delete=models.CASCADE, verbose_name = "Связанные файлы"
    )

    class Meta:
        verbose_name_plural = "Сотрудники"
        verbose_name = "сотрудника"
        ordering = ["position_var"]

    def __str__(self):
        return self.name
