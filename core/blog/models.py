from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.core.files.storage import FileSystemStorage
from django.forms.models import modelform_factory
from Uploads.models import Uploads

fs = FileSystemStorage(location="/files")


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    published = PublishedManager()
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    image = models.ImageField(upload_to="media", null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploads = models.ForeignKey(
        Uploads, null=True, blank=True, on_delete=models.CASCADE
    )
    status = models.TextField(
        max_length=10, choices=STATUS_CHOICES, null=True, blank=True
    )

    tags = TaggableManager()

    class Meta:
        ordering = ("-publish",)
        verbose_name_plural = "Добавление новостей"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            # "blog:post_list_by_tag",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
