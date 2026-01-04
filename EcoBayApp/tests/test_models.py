from EcoBayApp.models import User, Category, Item, Skill, Offer
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


class ItemTestModel(TestCase):
    def setUp(self):
        self.item = baker.make(Item)
    
    def test_item_created(self):
        self.assertIsNotNone(self.item.pk)
    
    def test_item_in_db(self):
        items = Item.objects.all()
        assert len(items) != 0

class SkillTestModel(TestCase):
    def setUp(self):
        self.skill = baker.make(Skill)
    
    def test_skill_created(self):
        self.assertIsNotNone(self.skill.pk)
    
    def test_skill_in_db(self):
        skills = Skill.objects.all()
        assert len(skills) != 0


class OfferTestModel(TestCase):
    def setUp(self):
        self.offer = baker.make(Offer)
    
    def test_offer_created(self):
        self.assertIsNotNone(self.offer.pk)
    
    def test_offer_in_db(self):
        offers = Offer.objects.all()
        assert len(offers) != 0