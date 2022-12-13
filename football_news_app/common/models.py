from django.db import models

from football_news_app.articles.models import Article


class Message(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField()


