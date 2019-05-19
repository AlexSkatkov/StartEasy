from django.test import TestCase, Client
from django.contrib.auth.models import User
from .forms import *
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

# Create your tests here.


class TestSuite(TestCase):

    def test_user_can_login(self):
        response = self.client.post("/login", {"username": "alexx", "password": "blabla123"})
        self.assertEquals(response.status_code, 301)
        r = self.client.get('/login')
        self.assertEquals(r.status_code, 301)               # when we open the site it redirects us to the login page

    def test_user_can_logout(self):
        self.client = Client()
        self.client.login(username='alex', password='12grbd732a')
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)


class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test1", email="blabl@gmail.com", password1="12grbd732a",
                                        password2="12grbd732a")


class User_Form_Test(TestCase):
    def test_register_form(self):                #checks valid form data
        form = UserRegisterForm(data={'username': "test1", 'email': "blabl@gmail.com", 'password1': "12grbd732a",
                                      'password2': "12grbd732a"})
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):        #checks invalid form data
        form = UserRegisterForm(data={'username': "", 'email': "mp", 'password1': "mp", 'password2': ""})
        self.assertFalse(form.is_valid())




class User_Views_Test(TestCase):

    def test_home_view(self):
        #tests the home view
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_add_user_view(self):
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")


class TestProfile(TestCase):
    def test_form(self):
        data = {'image': 'Foo'}
        form = ProfileUpdateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_post_404(self):
        c=Client()
        response=c.post('post_detail')
        self.assertEqual(response.status_code, 404)


#integration testing


class MySeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        #self.selenium.find_element_by_xpath('//input[@value=”Login”]').click()







