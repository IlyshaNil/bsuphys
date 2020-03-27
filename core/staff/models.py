from django.db import models
from Uploads.models import Uploads
from staff.staff_conf import choises


class Staff_unit(models.Model):
    name = models.TextField()
    position = models.TextField(null=True, blank=True)
    position_var = models.TextField(
        max_length=30, choices=choises.POSTION_CHOISES, null=True, blank=True
    )
    specialization = models.TextField(
        max_length=30, choices=choises.STATUS_CHOICES, null=True, blank=True
    )
    slug = models.URLField(max_length=250)
    image = models.ImageField(upload_to="media/staff", null=True, blank=True)
    description = models.TextField()
    uploads = models.ForeignKey(
        Uploads, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Сотрудники"


# Create your models here.
