from football_news_app.teams.models import Team


def get_team_by_name_and_pk(team_slug, pk):
    return Team.objects.filter(slug=team_slug, pk=pk).get()
