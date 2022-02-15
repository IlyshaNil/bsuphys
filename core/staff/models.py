from django.db import models
from Uploads.models import Uploads
from staff.staff_conf import choises
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _


class Staff_unit(models.Model):
    name = models.TextField()
    position = models.TextField(null=True, blank=True)
    academic_rank = models.TextField(null=True, blank=True)
    position_var = models.TextField(
        max_length=30, choices=choises.POSTION_CHOISES, null=True, blank=True
    )
    specialization = models.TextField(
        max_length=30, choices=choises.STATUS_CHOICES, null=True, blank=True
    )
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to="media/staff", null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    uploads = models.ForeignKey(
        Uploads, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Сотрудники"
        ordering = ['position_var']

    def __str__(self):
        return self.name