# Generated by Django 3.0.3 on 2020-03-07 09:09

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("slug", models.SlugField(blank=True, max_length=200)),
                ("url", models.URLField()),
                (
                    "image",
                    models.ImageField(
                        storage=django.core.files.storage.FileSystemStorage(
                            location="/files"
                        ),
                        upload_to="",
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("created", models.DateField(auto_now_add=True, db_index=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users_like",
                    models.ManyToManyField(
                        blank=True,
                        related_name="images_liked",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
