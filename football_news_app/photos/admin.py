from django.contrib import admin

from football_news_app.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'location', 'teams')
    list_filter = ('publication_date', 'location')

    @staticmethod
    def teams(current_photo_obj):
        tagged_teams = current_photo_obj.tagged_teams.all()
        if tagged_teams:
            return ', '.join(t.team_name for t in tagged_teams)
        return 'No teams'
