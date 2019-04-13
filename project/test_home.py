from unittest import TestCase
from django.urls import resolve,reverse
from .views import home
from django.test.client import Client


class TestHome(TestCase):

    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)


