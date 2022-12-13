from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from football_news_app.articles.forms import ArticleCommentForm
from football_news_app.articles.models import Article
from football_news_app.common.forms import ContactForm

from football_news_app.core.article_utils import apply_likes_count_articles, apply_user_liked_article, \
    apply_likes_count_photos
from football_news_app.photos.models import Photo


def index(request):
    user = request.user.pk
    articles = Article.objects.all()
    articles = [apply_likes_count_articles(article) for article in articles]
    articles = [apply_user_liked_article(article) for article in articles]
    photos = Photo.objects.all()
    photos = [apply_likes_count_photos(photo) for photo in photos]
    page = request.GET.get('page', 1)
    paginated_photos = Paginator(photos, 3)

    try:
        photos = paginated_photos.page(page)
    except PageNotAnInteger:
        photos = paginated_photos.page(1)
    except EmptyPage:
        photos = paginated_photos.page(paginated_photos.num_pages)

    context = {
        'user': user,
        'articles': articles,
        'photos': photos,
        'comment_form': ArticleCommentForm(),
    }
    return render(request, 'common/index-two.html', context, )


def show_contact_details(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('index')
    context = {
        'form': form
    }

    return render(request, 'common/contacts.html', context)



