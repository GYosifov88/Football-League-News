from django.contrib.auth import get_user_model
from tests.accounts.BaseTestCase import TestCaseBase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_match

UserModel = get_user_model()


class MatchesListViewsTest(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': 'Gy8804231022',
    }

    def test_matches_list_page__when_no_matches__expect_empty_matches(self):
        response = self.client.get(reverse_lazy('matches'))
        self.assertEmpty(response.context['matches'])

    def test_matches_list_page__when_1_match__expect_1_match(self):

        matches = create_match(count=1)

        response = self.client.get(reverse_lazy('matches'))

        self.assertEqual(1, len(response.context['matches']))
        self.assertListEqual(list(matches), list(response.context['matches']))

    def test_matches_list_page__when_5_matches__expect_5_matches(self):

        matches = create_match(count=5)

        response = self.client.get(reverse_lazy('matches'))

        self.assertEqual(5, len(response.context['matches']))
        self.assertListEqual(list(matches), list(response.context['matches']))


