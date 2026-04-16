from django.contrib import admin
from .models import Message, MessageRequest

# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "message", "created_at")
    list_filter = ("sender", "receiver", "created_at")
    search_fields = ("message", "sender__username", "receiver__username")

@admin.register(MessageRequest)
class MessageRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "accepted", "created_at")
    list_filter = ("accepted",)    