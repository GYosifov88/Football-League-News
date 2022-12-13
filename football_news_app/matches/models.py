from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from football_news_app.core.model_mixins import StrFromFieldsMixin

from football_news_app.core.validators import validate_file_less_than_7mb
from football_news_app.teams.models import Team


class Match(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo',)
    MAX_LEAGUE_NAME_LENGTH = 30
    MIN_LEAGUE_NAME_LENGTH = 2
    MAX_PLACE_NAME_LENGTH = 30
    MIN_PLACE_NAME_LENGTH = 2
    MAX_LEAGUE_STAGE_LENGTH = 30

    home_team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT,
        related_name='%(class)s_home_team',
    )

    guest_team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT,
        related_name='%(class)s_guest_team',
    )

    photo = models.ImageField(
        upload_to='matches-photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_7mb,),
    )

    league = models.CharField(
        max_length=MAX_LEAGUE_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LEAGUE_NAME_LENGTH),
        ),
        null=True,
        blank=True
    )

    match_date = models.DateField(
        blank=True,
        null=False,
    )

    match_location = models.CharField(
        max_length=MAX_PLACE_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_PLACE_NAME_LENGTH),
        ),
        null=True,
        blank=True
    )

    league_stage = models.CharField(
        max_length=MAX_LEAGUE_STAGE_LENGTH,
        blank=False,
        null=False,
    )

    def clean(self):
        if self.home_team == self.guest_team:
            raise ValidationError('Home team and Guest team should be different')

    def __str__(self):
        return f"{self.home_team} vs {self.guest_team}"



