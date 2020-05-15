from django.test import Client, TestCase
from django.urls import reverse


# Create your tests here.
class CoreTest(TestCase):
    def test_index(self):
        c = Client()
        response = c.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
