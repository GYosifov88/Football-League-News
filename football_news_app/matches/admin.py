from django.contrib import admin

from football_news_app.matches.models import Match


@admin.register(Match)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'guest_team', 'league', 'match_date', 'match_location',)
    list_filter = ('home_team', 'guest_team', 'league', 'match_date', 'match_location',)