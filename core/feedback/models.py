from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема отзыва')
    email = models.CharField(max_length=255, verbose_name='Контакт для обратной связи')
    content = models.TextField(verbose_name='Содержимое отзыва')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    ip_address = models.GenericIPAddressField(verbose_name='IP отправителя',  blank=True, null=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']

    def __str__(self):
        return f'Отзыв от {self.email}'
