from django.test import TestCase


# Create your tests here.
from users.models import User
from users.serializers import UserSerializer, UserInfoSerializer


class APITUserTest(TestCase):
    def setUp(self):
        self.user_attributes = {
            'username': 'apitest',
            'password': '123qweasd',
            'email': 'test@mail.com'
        }

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserInfoSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['id', 'email', 'username', 'role']))
