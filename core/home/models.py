from django.db import models

# Create your models here.

class MainPageStatisticNumber(models.Model):
    number = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
