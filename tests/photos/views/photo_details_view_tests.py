from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_photo_likes_for_user_and_photos, \
    create_photo_for_user


class PhotoDetailsViewsTests(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@petstagram.tk',
        'password': 'Gy8804231022',
    }

    def test_photo_details__when_no_likes_expect_0_likes_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        photos = create_photo_for_user(user, count=1)
        total_likes_count = 0
        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photos[0].pk}))
        self.assertEqual(total_likes_count, response.context['likes_count'])

    def test_photo_details__when_likes_expect_correct_likes_count(self):

        user = self._create_user_and_login(self.VALID_USER_DATA)
        photos = create_photo_for_user(user, count=1)
        total_likes_count = create_photo_likes_for_user_and_photos(user, photos)
        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photos[0].pk}))

        self.assertEqual(total_likes_count, response.context['likes_count'])