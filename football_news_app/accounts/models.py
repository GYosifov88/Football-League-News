from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from football_news_app.core.validators import validate_only_letters, validate_file_less_than_7mb


class AppUser(AbstractUser):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30
    DEFAULT_IMG = '/profile_photos/auser.jpg'

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        ],
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        ],
    )

    email = models.EmailField(
        unique=True,
    )

    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_7mb,),
        default=DEFAULT_IMG,
    )


