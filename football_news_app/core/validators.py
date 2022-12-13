from django.core import exceptions
from django.core.exceptions import ValidationError
from football_news_app.core.utils import megabyte_to_bytes


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')


def validate_file_less_than_7mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 7.0
    if filesize > megabyte_to_bytes(megabyte_limit):
        raise ValidationError(f"Max file size is {megabyte_limit}MB")

