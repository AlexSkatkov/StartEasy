from django.test import TestCase
from django.test.client import Client
from .forms import PostForm2,PostForm
from users.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

class TestPost_new(TestCase):

    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_form2(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm2(data=data)
        self.assertFalse(form.is_valid())

class TestPost_edit(TestCase):
    def test_form1(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form2(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm2(data=data)
        self.assertFalse(form.is_valid())

    def test_form2_fail(self):
        data = {'title': 'Foo', 'customer': 'Bar','author': 'alex' }
        form = PostForm2(data=data)
        self.assertTrue(not form.is_valid())

    def test_post_404(self):
        c=Client()
        response=c.post('post_detail')
        self.assertEqual(response.status_code, 404)


class TestPost_detail(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestPost_delete(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestPdf(TestCase):

    def test_redirect(self):
            c = Client()
            response = c.get(u'http://testserver/', follow=True)
            self.assertEqual(response.status_code, 200)

class TestHome(TestCase):

    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestHelp(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestAbout(TestCase):
    def test_about(self):
        data = {'from_email': 'Foo@gmail.com', 'subject': 'ofek', 'message': 'alex'}
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_email(self):
        subject = 'Some subject'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = 'This is my test message'
        recipient_list = ['mytest@gmail.com', 'you@email.com']
        html_message = '<h1>This is my HTML test</h1>'
        send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)

    def test_redirect_fail(self):
        c = Client()
        response = c.get('project/About', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestExamples(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestTips(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestComments(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)

class TestQA(TestCase):
    def test_redirect(self):
        c = Client()
        response = c.get(u'http://testserver/', follow=True)
        self.assertEqual(response.status_code, 200)