from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


from Uploads.models import Uploads

fs = FileSystemStorage(location="/files")


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    published = PublishedManager()
    STATUS_CHOICES = (
        ("draft", "draft"),
        ("published", "published"),
    )
    title = models.TextField(verbose_name = "Заголовок")
    slug = models.SlugField(max_length=250, unique_for_date="publish", verbose_name = "Слаг")
    image = models.ImageField(upload_to="media", null=True, blank=True, verbose_name = "Афиша")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name = "Автор"
    )
    body = RichTextField(verbose_name = "Контент")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Дата публикации")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploads = models.ForeignKey(
        Uploads, null=True, blank=True, on_delete=models.CASCADE, verbose_name = "Прикрепленные файлы"
    )
    status = models.TextField(
        max_length=10,
        choices=STATUS_CHOICES,
        null=True,
        blank=True,
        help_text="Обязательное поле!",
        verbose_name = "Статус"
    )

    

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = "Добавление новостей"
        verbose_name = "новость"

    def __str__(self):
        return self.title

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = "Афиша"
    admin_photo.allow_tags = True

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class NoteInMedia(models.Model):
    published = PublishedManager()
    STATUS_CHOICES = (
        ("draft", "Черновик"),
        ("published", "Опубликовать"),
    )
    title = models.TextField(verbose_name = "Заголовок")
    slug = models.SlugField(max_length=250, unique_for_date="publish", verbose_name = "Слаг")
    image = models.ImageField(upload_to="media", null=True, blank=True, verbose_name = "Изображение")
    body = RichTextField(verbose_name = "Текст")
    status = models.TextField(
        max_length=10,
        choices=STATUS_CHOICES,
        null=True,
        blank=True,
        help_text="Обязательное поле!",
        verbose_name = "Статус"
    )
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Дата публикации")

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = "Новые заметки в СМИ"
        verbose_name = "заметку"

    def __str__(self):
        return self.title

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = "Афиша"
    admin_photo.allow_tags = True
