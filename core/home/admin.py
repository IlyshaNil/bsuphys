from django.contrib import admin
from .models import MainPageStatisticNumber
# Register your models here.


@admin.register(MainPageStatisticNumber)
class MainPageStaticNumbersAdmin(MainPageStatisticNumber):
    list_display = ["number", "description"]
    list_filter = ["number", "description"]

    class Meta:
        verbose_name_plural = "Физический факультет в цифрах"
