from unittest import TestCase
from django.test.client import Client
from .forms import PostForm2

class TestPost_new(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_form2(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm2(data=data)
        self.assertTrue(form.is_valid())