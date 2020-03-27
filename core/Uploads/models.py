from django.db import models

from django.db import models


class Uploads(models.Model):
    file = models.FileField(upload_to="media/")
    title = models.TextField()
    created = models.DateField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = "Загрузка файлов"

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.pk}: {self.title}"

    def __str__(self):
        return f"{self.title} ({self.pk})"
