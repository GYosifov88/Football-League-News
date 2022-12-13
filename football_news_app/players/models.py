from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from football_news_app.core.model_mixins import StrFromFieldsMixin, ChoicesEnumMixin
from football_news_app.core.validators import validate_file_less_than_7mb
from football_news_app.teams.models import Team

UserModel = get_user_model()


class Position(ChoicesEnumMixin, Enum):
    goalkeeper = 'Goalkeeper'
    defender = 'Defender'
    midfielder = 'Midfielder'
    attacker = 'Attacker'


class Player(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_FIRST_NAME = 50
    MAX_LAST_NAME = 50
    MAX_LEN_NATIONALITY = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME,
        null=False,
        blank=False,
    )

    personal_photo = models.ImageField(
        upload_to='players_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_7mb,),
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    biography = models.TextField(
        null=False,
        blank=False,
    )

    position = models.CharField(
        choices=Position.choices(),
        max_length=Position.max_len(),
    )

    nationality = models.CharField(
        max_length=MAX_LEN_NATIONALITY,
        null=False,
        blank=False,
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT,
    )

    team_number = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    rating = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    goals = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    assists = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    matches = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.first_name}-{self.last_name}')
        return super().save(*args, **kwargs)

