from django.contrib.auth import get_user_model
from tests.accounts.BaseTestCase import TestCaseBase
from django.urls import reverse_lazy

from tests.utils.creation_utils import create_photo_for_user

UserModel = get_user_model()


class PhotoListViewsTest(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': 'Gy8804231022',
    }

    def test_photo_list_page__when_no_photos__expect_empty_photos(self):
        response = self.client.get(reverse_lazy('show photos'))
        self.assertEmpty(response.context['photos'])

    def test_photo_list_page__when_1_photo__expect_1_photo(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        photos = create_photo_for_user(user, count=1)

        response = self.client.get(reverse_lazy('show photos'))

        self.assertEqual(1, len(response.context['photos']))
        self.assertListEqual(list(photos), list(response.context['photos']))

    def test_photo_list_page__when_2_photos__expect_2_photos(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        photos = create_photo_for_user(user, count=2)

        response = self.client.get(reverse_lazy('show photos'))

        self.assertEqual(2, len(response.context['photos']))
        self.assertListEqual(list(photos), list(response.context['photos']))


