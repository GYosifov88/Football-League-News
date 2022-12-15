from django.contrib.auth import get_user_model
from tests.accounts.BaseTestCase import TestCaseBase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_players

UserModel = get_user_model()


class PlayersListViewsTest(TestCaseBase):

    def test_players_list_page__when_no_players__expect_empty_players(self):
        response = self.client.get(reverse_lazy('players'))
        self.assertEmpty(response.context['players'])

    def test_players_list_page__when_1_player__expect_1_player(self):
        players = create_players(count=1)

        response = self.client.get(reverse_lazy('players'))

        self.assertEqual(1, len(response.context['players']))
        self.assertListEqual(list(players), list(response.context['players']))

    def test_players_list_page__when_5_players__expect_5_players(self):

        players = create_players(count=5)

        response = self.client.get(reverse_lazy('players'))

        self.assertEqual(5, len(response.context['players']))
        self.assertListEqual(list(players), list(response.context['players']))


