from django.contrib.auth.models import User, AnonymousUser
from django.test import RequestFactory, TestCase
from .models import Storie, Comment


class TestStorie(TestCase):

    def setUpStorie(self):
        Storie.objects.create(title='some title', author='fullname')
        self.assertFalse(storie.done)
    