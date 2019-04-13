from unittest import TestCase
from django.test.client import Client

class TestPdf(TestCase):

    def test_redirect(self):
            c = Client()
            response = c.get(u'http://testserver/', follow=True)
            self.assertEqual(response.status_code, 200)
