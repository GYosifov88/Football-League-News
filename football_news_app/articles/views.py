from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from . import models
from django.shortcuts import render, redirect
from django.views.generic import ListView

from football_news_app.articles.models import Article, ArticleLike
from .forms import ArticleCommentForm
from football_news_app.articles.utils import get_article_url
from ..teams.models import Team


class ArticlesListView(ListView):
    context_object_name = 'articles'
    model = models.Article
    template_name = 'articles/news-large.html'
    articles_paginate_by = 3

    def get_article_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_articles(self):
        page = self.get_article_page()
        articles = self.object_list.all().order_by('-publication_date')
        paginator = Paginator(articles, self.articles_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, *args, **kwargs,):
        context = super().get_context_data(*args, **kwargs)
        context['teams'] = Team.objects.all()
        context['articles'] = self.get_paginated_articles()

        return context


def details_article(request, pk):
    article = Article.objects.filter(pk=pk).get()
    is_liked_by_user = article.articlelike_set.filter(user_id=request.user.id) \
        .exists()
    context = {
        'article': article,
        'is_liked': is_liked_by_user,
        'likes_count': article.articlelike_set.count(),
        'is_owner': request.user == article.user,
        'comments': article.articlecomment_set.all(),
        'comments_count': article.articlecomment_set.count(),
    }

    return render(request, 'articles/news-details.html', context)


@login_required
def like_article(request, article_pk):
    user_liked_articles = ArticleLike.objects.filter(
        article_id=article_pk,
        user_id=request.user.pk,
    )

    if user_liked_articles:
        user_liked_articles.delete()
    else:

        ArticleLike.objects.create(
            article_id=article_pk,
            user_id=request.user.pk,
        )

    return redirect(get_article_url(request, article_pk))


@login_required
def comment_article(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.filter(pk=article_pk).get()
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()

    return redirect(get_article_url(request, article_pk))

