
from django.test import TestCase
from django.urls import reverse
#test case for home view 
class SimpleTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Welcome to the Task Manager API!")
