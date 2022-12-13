from django.urls import path

from football_news_app.teams.views import TeamsListView, details_team

urlpatterns = (
    path('', TeamsListView.as_view(), name='teams'),
    path('<int:pk>/<slug:team_slug>/', details_team, name='team details'),
)
