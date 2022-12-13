from football_news_app.players.models import Player


def get_player_by_name_and_pk(player_slug, pk):
    return Player.objects.filter(slug=player_slug, pk=pk).get()
