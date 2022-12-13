from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('football_news_app.accounts.urls')),
    path('', include('football_news_app.common.urls')),
    path('articles/', include('football_news_app.articles.urls')),
    path('matches/', include('football_news_app.matches.urls')),
    path('players/', include('football_news_app.players.urls')),
    path('teams/', include('football_news_app.teams.urls')),
    path('photos/', include('football_news_app.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

