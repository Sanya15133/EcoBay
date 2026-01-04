from EcoBayApp.models import User, Category, Item, Skill
from django.test import TestCase
from model_bakery import baker

class UserTestModel(TestCase):
    def setUp(self):
        self.user = baker.make(User)
    
    def test_user_created(self):
        self.assertIsNotNone(self.user.pk)
    
    def test_user_in_db(self):
        users = User.objects.all()
        assert len(users) != 0    


class CategoryTestModel(TestCase):
    def setUp(self):
        self.category = baker.make(Category)
    
    def test_category_created(self):
        self.assertIsNotNone(self.category.pk)
    
    def test_category_in_db(self):
        categories = Category.objects.all()
        assert len(categories) != 0


