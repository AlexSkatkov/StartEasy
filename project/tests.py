from django.test import TestCase,Client
from django.urls import reverse
from StartEasy.project import views,urls


class Test_Views(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')

    def test_views_home(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/home.html')

     def test_views_post_new_POST(self):
