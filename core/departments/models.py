from ckeditor.fields import RichTextField
from django.db import models
from staff.models import Staff_unit

# Create your models here.
class Department(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to="media", null=True, blank=True)
    short_description = RichTextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    thesis_themes = RichTextField(null=True, blank=True)
    science_directions = RichTextField(null=True, blank=True)
    publications = RichTextField(null=True, blank=True)
    courses = RichTextField(null=True, blank=True)
    staff = models.ManyToManyField(Staff_unit)
    slug = models.SlugField(max_length=250)
