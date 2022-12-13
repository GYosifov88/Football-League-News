from django.core.paginator import Paginator

from . import models
from django.shortcuts import render
from django.views.generic import ListView

from .models import Player
from .utils import get_player_by_name_and_pk
from ..teams.models import Team


class PlayersListView(ListView):
    context_object_name = 'players'
    model = models.Player
    template_name = 'players/team-players-list.html'
    players_paginate_by = 6

    def get_players_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_players(self):
        page = self.get_players_page()
        players = self.object_list.all().order_by('-rating')
        paginator = Paginator(players, self.players_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['teams'] = Team.objects.all()
        context['players'] = self.get_paginated_players()

        return context


def details_player(request, player_slug, pk):
    player = get_player_by_name_and_pk(player_slug, pk)

    context = {
        'player': player,
    }

    return render(request, 'players/player-details.html', context)
