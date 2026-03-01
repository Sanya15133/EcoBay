from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()


class MyHomeViewsTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'skills')
    
    def test_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")
    
    def test_search_bar(self):
        response = self.client.get('/search/', {'query': 'laptop'})
        self.assertEqual(response.status_code, 200)
    
    def test_search_item_not_found(self):
        query = 'random_item'
        response = self.client.get('/search/', {'search': query})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,  f'No results found for {query}')
    

class MyRegisterViewsTests(TestCase):
    
    def test_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'register.html')
    
    def test_user_posts(self):
        response = self.client.post('/register/', {
            'username': 'sanya',
            'email': '123@mail.com',
            'password': '123qwer',
            'confirm_password': '123qwer'
        })
        self.assertEqual(response.status_code, 302)

    def test_user_exists(self):

        User.objects.create_user(
            username='Sanya',
            email='123@mail.com',
            password='123qwer'
        )

        response = self.client.post('/register/', {
            'username': 'Sanya',
            'email': '123@mail.com',
            'password': '123qwer',
            'confirm_password': '123qwer'
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User already exists")
    

class MyLoginViewsTest(TestCase):

    def test_login_template_renders(self):
        response = self.client.get(reverse('login_view'))
        self.assertTemplateUsed(response, 'login.html')
    
    def test_login_works(self):

        User.objects.create_user(
            username='test_user',
            email='123@mail.com',
            password='123qwer'
        )
    
        self.client.login(username='test_user', password='123qwer')
        response = self.client.get('/add-item/')
        self.assertEqual(response.status_code, 200)

    def test_incorrect_login_details(self):

        response = self.client.post(reverse('login_view'), {
            'username': 'non_user',
            'password': '123qwer'
        })

        self.assertContains(response, "Invalid username and/or password.")
