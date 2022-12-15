from django.contrib.auth import get_user_model
from tests.accounts.BaseTestCase import TestCaseBase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_article_for_user

UserModel = get_user_model()


class ArticlesListViewsTest(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': 'Gy8804231022',
    }

    def test_articles_list_page__when_no_articles__expect_empty_articles(self):
        response = self.client.get(reverse_lazy('articles'))
        self.assertEmpty(response.context['articles'])

    def test_articles_list_page__when_1_article__expect_1_articles(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        articles = create_article_for_user(user, count=1)

        response = self.client.get(reverse_lazy('articles'))

        self.assertEqual(1, len(response.context['articles']))
        self.assertListEqual(list(articles), list(response.context['articles']))

    def test_articles_list_page__when_2_articles__expect_2_articles(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        articles = create_article_for_user(user, count=2)

        response = self.client.get(reverse_lazy('articles'))

        self.assertEqual(2, len(response.context['articles']))
        self.assertListEqual(list(articles), list(response.context['articles']))


