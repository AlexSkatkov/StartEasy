from unittest import TestCase
from .forms import ProfileUpdateForm,UserUpdateForm
from django.test import Client

class TestProfile(TestCase):
    def test_form1(self):
        data = {'image': 'Foo'}
        form = ProfileUpdateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form2(self):
        data = {'email': 'Foo@gmail.com'}
        form = UserUpdateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_post_404(self):
        c=Client()
        response=c.post('post_detail')
        self.assertEqual(response.status_code, 404)


