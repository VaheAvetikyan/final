from django.test import TestCase
from django.db.models import Max
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError

from .models import User


# Create your tests here.
class AuthTest(TestCase):
    def setUp(self):
        User.objects.create_user(email="test@mail.com", first_name="test", last_name="test", password="password123")

    def test_user_count(self):
        user = User.objects.filter(email="test@mail.com")
        self.assertEqual(user.count(), 1)

    def test_check_authentication(self):
        user = authenticate(email="test@mail.com", password="password123")
        self.assertTrue(user)

    def test_check_no_authentication(self):
        user = authenticate(email="test@mail.com", password="wrong_password")
        self.assertFalse(user)

    def test_same_email(self):
        try:
            User.objects.create(email="test@mail.com", first_name="test", last_name="test", password="password123")
            self.fail("Created user with not unique email")
        except IntegrityError:
            pass

    def test_user_no_first_name(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="test1@mail.com", last_name="test", password="password123")

    def test_user_name_space(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="test1@mail.com", first_name=" ", last_name=" ", password="password123")

    def test_check_password_for_strength(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="test1@mail.com", first_name="test", last_name="test", password="pass")
