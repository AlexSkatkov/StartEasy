from django.test import TestCase,Client
from django.urls import reverse
from StartEasy import project

import json

class Test_Views(TestCase):
    def test_views_home(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/home.html')