from django.urls import path

from football_news_app.matches.views import details_match
from football_news_app.matches.views import MatchesListView

urlpatterns = (
    path('', MatchesListView.as_view(), name='matches'),
    path('<int:pk>/', details_match, name='match details'),
)
