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
        ("draft", "Черновик"),
        ("published", "Опубликовать"),
    )
    title = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    image = models.ImageField(upload_to="media", null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploads = models.ForeignKey(
        Uploads, null=True, blank=True, on_delete=models.CASCADE
    )
    status = models.TextField(
        max_length=10, choices=STATUS_CHOICES, null=True, blank=True, help_text="Обязательное поле!"
    )

    tags = TaggableManager()

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = "Добавление новостей"

    def __str__(self):
        return self.title

    def admin_photo(self):
        return  mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description = "Афиша"
    admin_photo.allow_tags = True

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            # "blog:post_list_by_tag",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class NoteInMedia(models.Model):
    published = PublishedManager()
    STATUS_CHOICES = (
        ("draft", "Черновик"),
        ("published", "Опубликовать"),
    )
    title = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    image = models.ImageField(upload_to="media", null=True, blank=True)
    body = RichTextField()
    status = models.TextField(
        max_length=10, choices=STATUS_CHOICES, null=True, blank=True, help_text="Обязательное поле!"
    )
    publish = models.DateTimeField(default=timezone.now, )

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = "Новые заметки в СМИ"

    def __str__(self):
        return self.title

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    admin_photo.short_description = "Афиша"
    admin_photo.allow_tags = True

