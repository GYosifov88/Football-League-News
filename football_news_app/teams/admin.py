from django.contrib import admin

from football_news_app.teams.models import Team


@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
    list_display = ('team_name',)
    list_filter = ('team_name',)
