from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from football_news_app.core.model_mixins import StrFromFieldsMixin
from football_news_app.core.validators import validate_file_less_than_7mb

from football_news_app.teams.models import Team

UserModel = get_user_model()


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='football_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_7mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True
    )
    location = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LOCATION_LENGTH,
    )

    publication_date = models.DateField(
        auto_now=True,
        blank=True,
        null=False,
    )

    tagged_teams = models.ManyToManyField(
        Team,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )