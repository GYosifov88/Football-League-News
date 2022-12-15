from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_article_for_user, create_articles_likes_for_user_and_article, \
    create_articles_comments_for_user_and_article


class ArticleDetailsViewsTests(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': 'Gy8804231022',
    }

    def test_article_details__when_no_likes_expect_0_likes_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        articles = create_article_for_user(user, count=1)
        total_likes_count = 0
        response = self.client.get(reverse_lazy('article details', kwargs={'pk': articles[0].pk}))
        self.assertEqual(total_likes_count, response.context['likes_count'])

    def test_article_details__when_likes_expect_correct_likes_count(self):

        user = self._create_user_and_login(self.VALID_USER_DATA)
        articles = create_article_for_user(user, count=1)
        total_likes_count = create_articles_likes_for_user_and_article(user, articles)
        response = self.client.get(reverse_lazy('article details', kwargs={'pk': articles[0].pk}))

        self.assertEqual(total_likes_count, response.context['likes_count'])


    def test_article_details__when_no_comments_expect_0_comments_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        articles = create_article_for_user(user, count=1)
        total_comments_count = 0
        response = self.client.get(reverse_lazy('article details', kwargs={'pk': articles[0].pk}))
        self.assertEqual(total_comments_count, response.context['comments_count'])

    def test_article_details__when_comments_expect_correct_comments_count(self):

        user = self._create_user_and_login(self.VALID_USER_DATA)
        articles = create_article_for_user(user, count=1)
        total_comments_count = create_articles_comments_for_user_and_article(user, articles)
        response = self.client.get(reverse_lazy('article details', kwargs={'pk': articles[0].pk}))

        self.assertEqual(total_comments_count, response.context['comments_count'])