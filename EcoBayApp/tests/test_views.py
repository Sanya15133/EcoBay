from django.test import TestCase
from django.urls import reverse

class MyViewsTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")
    
    def test_search_bar(self):
        response = self.client.get('/search/', {'query': 'laptop'})
        self.assertEqual(response.status_code, 200)
    

