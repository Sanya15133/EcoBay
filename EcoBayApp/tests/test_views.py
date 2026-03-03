from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
from EcoBayApp.models import Item, Skill, Category

class LoadFixtures(TestCase):
    fixtures = ['categories.json', 'items.json']

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

    def test_incorrect_login_details_return_error(self):

        response = self.client.post(reverse('login_view'), {
            'username': 'non_user',
            'password': '123qwer'
        })

        self.assertContains(response, "Invalid username and/or password.")

    def test_logout_view(self):

        User.objects.create_user(
            username='test_user',
            email='123@mail.com',
            password='123qwer'
        )

        self.client.login(username='test_user', password='123qwer')
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class MyItemViewsTest(TestCase):

    def test_get_items(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'items')
    
    def test_get_item_by_id(self):
        
        user = User.objects.create_user(
        username='test_user',
        password='123qwer'
    )

        category = Category.objects.create(
        name='Electronics'
    )

        item = Item.objects.create(
            name='remote',
            description='used remote, needs batteries',
            amount='5',
            image_url='https://c8.alamy.com/comp/E91P3W/smashed-remote-control-E91P3W.jpg',
            category=category,
            user=user
    )

        self.client.login(username='test_user', password='123qwer')
        response = self.client.get(f'/item/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'remote')
    
    def test_incorrect_id(self):

        response = self.client.get(f'/item/7890/')
        self.assertEqual(response.status_code, 404)


    def test_add_item(self):

        self.user = User.objects.create_user(
            username='test_user',
            password='123qwer'
        )

        self.category = Category.objects.create(
            name='Electronics'
        )

        Item.objects.create(
            name='remote',
            description='used remote, needs batteries',
            amount='5',
            image_url='https://c8.alamy.com/comp/E91P3W/smashed-remote-control-E91P3W.jpg',
            category=self.category,
            user=self.user
        )

        self.client.login(username='test_user', password='123qwer')
        response = self.client.post('/add-item/', {
            'name':'remote',
            'description': 'used remote, needs batteries',
            'amount': '5',
            'image_url': 'https://c8.alamy.com/comp/E91P3W/smashed-remote-control-E91P3W.jpg',
            'category': self.category.id        
        })

        self.assertEqual(response.status_code, 200)

    def test_delete_item_by_id(self):

        self.user = User.objects.create_user(
            username='test_user',
            password='123qwer'
        )

        self.category = Category.objects.create(
            name='Electronics'
        )

        Item.objects.create(
            name='remote',
            description='used remote, needs batteries',
            amount='5',
            image_url='https://c8.alamy.com/comp/E91P3W/smashed-remote-control-E91P3W.jpg',
            category=self.category,
            user=self.user
        )

        self.client.login(username='test_user', password='123qwer')
        response = self.client.post('/add-item/', {
            'name':'remote',
            'description': 'used remote, needs batteries',
            'amount': '5',
            'image_url': 'https://c8.alamy.com/comp/E91P3W/smashed-remote-control-E91P3W.jpg',
            'category': self.category.id        
        })

        self.assertEqual(response.status_code, 200)
        item = Item.objects.get(id=1)
        self.client.delete(f'/item/delete/{item.id}')
        response_get = self.client.get(f'/item/{item.id}/')
        self.assertEqual(response_get.status_code, 404)

class MySkillViewsTest(TestCase):

    def test_get_skills(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'skills')
    
    def test_get_skill_by_id(self):
        
        user = User.objects.create_user(
        username='test_user',
        password='123qwer'
    )

        category = Category.objects.create(
        name='Baking'
    )

        skill = Skill.objects.create(
            name='baking cake',
            description='needs to look disney themed',
            amount='5',
            category=category,
            user=user
    )

        self.client.login(username='test_user', password='123qwer')
        response = self.client.get(f'/skill/{skill.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'baking cake')
    
    def test_incorrect_id(self):

        response = self.client.get(f'/skill/7890/')
        self.assertEqual(response.status_code, 404)


    def test_add_skill(self):

        self.user = User.objects.create_user(
        username='test_user',
        password='123qwer'
    )

        self.category = Category.objects.create(
        name='Baking'
    )

        self.client.login(username='test_user', password='123qwer')

        skill = Skill.objects.create(
            name='baking cake',
            description='needs to look disney themed',
            amount='5',
            category=self.category,
            user=self.user
    )

        response = self.client.post('/add-skill/', {
            'name': 'baking cake',
            'description': 'needs to look disney themed',
            'amount': '5',
            'category': self.category.id        
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/') 
        self.assertContains(response, 'baking cake')
