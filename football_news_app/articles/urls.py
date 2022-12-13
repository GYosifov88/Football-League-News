from django.urls import path

from football_news_app.articles.views import details_article, ArticlesListView, like_article, comment_article

urlpatterns = (
    path('', ArticlesListView.as_view(), name='articles'),
    path('<int:pk>/', details_article, name='article details'),
    path('like/<int:article_pk>/', like_article, name='like article'),
    path('comment/<int:article_pk>/', comment_article, name='comment article'),
)
