from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'type',
        'is_read',
        'created_at',
    )

    list_filter = (
        'type',
        'is_read',
        'created_at',
    )

    search_fields = (
        'title',
        'message',
        'user__username',
    )
from django.db import models


class Notifications(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
