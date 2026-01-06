from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    
class Item(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    image_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Skill(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Offer(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




    