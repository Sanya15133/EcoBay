from django.test import TestCase

class MyViewsTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_search_bar(self):
        response = self.client.get('/search/', {'query': 'cat'})
        self.assertEqual(response.status_code, 200)