# Generated by Django 3.0.8 on 2021-02-05 19:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0002_auto_20210205_1949"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff_unit",
            name="address_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="staff_unit",
            name="address_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="staff_unit",
            name="description_en",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="staff_unit",
            name="description_ru",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="staff_unit", name="name_en", field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="staff_unit", name="name_ru", field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="staff_unit",
            name="position_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="staff_unit",
            name="position_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="staff_unit",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
