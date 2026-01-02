from EcoBayApp.models import User, Category, Item, Skill
from django.test import TestCase
from model_bakery import baker

class UserTestModel(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        print(self.user)
    
    def test_user_created(self):
        self.assertIsNotNone(self.user.pk)
    
    def test_user_in_db(self):
        users = User.objects.all()
        print(users)
