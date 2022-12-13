from django.contrib import admin

from football_news_app.common.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'sender',)
    list_filter = ('subject', 'sender',)
