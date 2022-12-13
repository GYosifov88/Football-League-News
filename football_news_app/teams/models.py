from django.db import models
from django.template.defaultfilters import slugify

from football_news_app.core.model_mixins import StrFromFieldsMixin


class Team(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_TEAM_NAME = 30
    MAX_STADIUM_NAME = 40

    team_name = models.CharField(
        max_length=MAX_TEAM_NAME,
        null=False,
        blank=False,
    )
    team_logo_photo = models.URLField(
        null=False,
        blank=False,
    )

    stadium = models.CharField(
        max_length=MAX_STADIUM_NAME,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.team_name}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.team_name
