from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ('email', 'ip_address')
    list_display_links = ('email', 'ip_address')
