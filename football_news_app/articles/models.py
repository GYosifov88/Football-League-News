from django.contrib.auth import get_user_model
from django.db import models

from football_news_app.core.model_mixins import StrFromFieldsMixin
from football_news_app.core.validators import validate_file_less_than_7mb

from football_news_app.teams.models import Team

UserModel = get_user_model()


class Article(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'title')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 500
    MAX_AUTHOR_NAME = 40
    MAX_LEN_TITLE = 40

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        blank=False,
        null=False
    )

    author = models.CharField(
        max_length=MAX_AUTHOR_NAME,
        blank=False,
        null=False
    )

    photo = models.ImageField(
        upload_to='articles_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_7mb,),
    )

    description = models.TextField()

    publication_date = models.DateField(
        auto_now=True,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class ArticleComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,)

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class ArticleLike(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

