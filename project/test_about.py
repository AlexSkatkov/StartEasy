from unittest import TestCase
from users.forms import ContactForm
from django.test.client import Client

class TestAbout(TestCase):
    def test_about(self):
        data = {'from_email': 'Foo@gmail.com', 'subject': 'ofek', 'message': 'alex'}
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_redirect_fail(self):
        c = Client()
        response = c.get('project/About', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)
