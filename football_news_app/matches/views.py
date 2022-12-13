from django.core.paginator import Paginator

from . import models
from django.shortcuts import render
from django.views.generic import ListView

from .models import Match
from ..players.models import Player
from ..teams.models import Team


class MatchesListView(ListView):
    context_object_name = 'matches'
    model = models.Match
    template_name = 'matches/match-result-layout-2.html'
    matches_paginate_by = 5

    def get_matches_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_matches(self):
        page = self.get_matches_page()
        matches = self.object_list.all()
        paginator = Paginator(matches, self.matches_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, *args, **kwargs, ):
        context = super().get_context_data(*args, **kwargs)
        context['teams'] = Team.objects.all()
        context['matches'] = self.get_paginated_matches()
        return context


def details_match(request, pk):
    match = Match.objects.filter(pk=pk).get()
    home_players = Player.objects.filter(team=match.home_team)
    guest_players = Player.objects.filter(team=match.guest_team)
    home_players = home_players.order_by('team_number')
    context = {
        'match': match,
        'home_players': home_players,
        'guest_players': guest_players,
    }

    return render(request, 'matches/match-details.html', context)
