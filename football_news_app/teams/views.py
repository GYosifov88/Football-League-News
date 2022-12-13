from django.shortcuts import render
from django.views.generic import ListView

from . import models
from .utils import get_team_by_name_and_pk
from ..players.models import Player


class TeamsListView(ListView):
    context_object_name = 'teams'
    model = models.Team
    template_name = 'teams/point-table.html'


def details_team(request, team_slug, pk):
    team = get_team_by_name_and_pk(team_slug, pk)
    players = Player.objects.filter(team=team)
    context = {
        'team': team,
        'players': players,
    }

    return render(request, 'teams/upcoming-match.html', context)
