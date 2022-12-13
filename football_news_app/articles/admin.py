from django.contrib import admin

from football_news_app.articles.models import Article, ArticleComment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'publication_date', 'description')


@admin.register(ArticleComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user',)
