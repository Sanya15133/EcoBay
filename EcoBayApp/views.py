from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate
from .models import Item, Skill, User


def home(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'GET':
        query = request.form.get('search')

def register(request):
    
    if request.method == 'POST':
        username = request.form.post('username')
        email = request.form.post('email')
        password = request.form.post('name')
        confirm_password = request.form.post('name')

        if password != confirm_password:
            return render(request, 'register.html', {
                'message': 'Passwords do not match'
            })

        new_user = User({username, email, password, confirm_password})

    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.form.post('username')
        password = request.form.post('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "register.html")

def logout(request):
    logout(request)
    return redirect('index')

def item_categories(request):
    if request.method == 'GET':
        categories = categories.db

def list_items(request):
    if request.method == 'GET':
        items = Item.db.all()

def list_items_by_category(request):
    if request.method == 'GET':
        items = Item.db.all()

def add_item(request):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        bids = request.form.get('bids')
        image = request.form.get('image')

        new_item = Item({name, description, price, bids, image})

def get_item(request):
    if request.method == 'GET':
        query = request.form.get('item')
        item = Item.db.filter(query)

def list_skills(request):
    if request.method == 'GET':
        skills = Skill.db.all()

def add_skill(request):
    if request.method == 'POST':
        skill = request.form.get('skill')
        description = request.form.get('description')
        date = request.form.get('date')
        new_skill = Skill({skill, description, date})

def request_skill(request):
    if request.method == 'POST':
        print('hello')

def bid(request):
    if request.method == 'POST':
        print('bid')