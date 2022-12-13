from django.urls import path

from football_news_app.players.views import PlayersListView, details_player

urlpatterns = (
    path('', PlayersListView.as_view(), name='players'),
    path('<int:pk>/<slug:player_slug>/', details_player, name='player details'),
)
