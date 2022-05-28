from django.test import TestCase

# Create your tests here.


from django.test import TestCase, Client
from django.urls import reverse
import json
from accounts.models import User


class TestViews(TestCase):
     def setUp(self):
        print("set up is gonna execute")
        self.client=Client()
        self.user = User.objects.create_user(email='testuser@mail.com',password='123456')
        self.user.set_password("123456")
        self.user.save()

     def test_spaces_homepage_GET(self):
       self.client.login(email='testuser@mail.com', password='123456')
       response=self.client.get(reverse('homepage'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response,"spaces/homepage.html")
       
