# Generated by Django 3.0.8 on 2020-08-25 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advertisement",
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
                ("title", models.TextField(blank=True, null=True)),
                ("body", models.TextField(blank=True, null=True)),
                ("publish", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="QuantumCourse",
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
                ("name", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "timeTable",
                    models.ImageField(blank=True, null=True, upload_to="media"),
                ),
                ("lectionsUrl", models.URLField(blank=True, null=True)),
                ("consultationUrl", models.URLField(blank=True, null=True)),
                ("taskUrl", models.URLField(blank=True, null=True)),
                (
                    "course",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("1", "Квант-олимпиец"),
                            ("2", "Квант XI"),
                            ("3", "Квант X"),
                            ("4", "Квант IX"),
                            ("5", "Квант-юни"),
                        ],
                        help_text="Обязательное поле!",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "advertisement",
                    models.ManyToManyField(to="quantum_School.Advertisement"),
                ),
            ],
        ),
    ]
