from django.contrib import admin

from football_news_app.players.models import Player


@admin.register(Player)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'nationality', 'team')
    list_filter = ('position', 'nationality', 'team')
