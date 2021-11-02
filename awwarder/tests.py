from django.test import TestCase
from django.test import Editor
from django.test import Profile
# Create your tests here.
from django.test import TestCase
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Hope= Editor(bio = 'software developer')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Hope,Profile))