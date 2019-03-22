from unittest import TestCase
from django.test import Client

from .forms import PostForm,PostForm2
from .models import Post

class TestPost_edit(TestCase):
    def test_form1(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form2(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm2(data=data)
        self.assertTrue(form.is_valid())

    def test_form2_fail(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm2(data=data)
        self.assertFalse(form.is_valid())

    def test_post_404(self):
        c=Client()
        response=c.post('post_detail')
        self.assertEqual(response.status_code, 404)


