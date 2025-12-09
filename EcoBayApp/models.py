from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Skill(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)


class Offer(models.Model):
    id = models.CharField(max_length=40, unique=True, primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    