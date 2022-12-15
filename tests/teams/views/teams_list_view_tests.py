from django.contrib.auth import get_user_model
from tests.accounts.BaseTestCase import TestCaseBase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_teams

UserModel = get_user_model()


class TeamListViewsTest(TestCaseBase):

    def test_team_list_page__when_no_teams__expect_empty_teams(self):
        response = self.client.get(reverse_lazy('teams'))
        self.assertEmpty(response.context['teams'])

    def test_team_list_page__when_1_team__expect_1_team(self):
        teams = create_teams(count=1)
        response = self.client.get(reverse_lazy('teams'))

        self.assertEqual(1, len(response.context['teams']))
        self.assertListEqual(list(teams), list(response.context['teams']))

    def test_team_list_page__when_14_teams__expect_14_teams(self):
        teams = create_teams(count=14)

        response = self.client.get(reverse_lazy('teams'))

        self.assertEqual(14, len(response.context['teams']))
        self.assertListEqual(list(teams), list(response.context['teams']))


