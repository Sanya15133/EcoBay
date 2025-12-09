from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'index.html')

def search(request):
    
    if request.method == 'GET':
        query = request.form.get('search')

def register(request):
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('name')
        confirm_password = request.form.get('name')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    return render(request, 'sign-in.html')

def logout(request):
    logout(request)
    return redirect('index')

def item_categories(request):
    if request.method == 'GET':
        categories = categories.db

def list_items(request):
    if request.method == 'GET':
        items = items.db

def list_items_by_category(request):
    if request.method == 'GET':
        items = items.db

def add_item(request):
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        bids = request.form.get('bids')
        image = request.form.get('image')

def get_item(request):
    if request.method == 'GET':
        query = request.form.get('item')
        item = items.db.filter(query)

def list_skills(request):
    if request.method == 'GET':
        skills = skills.db

def add_skill(request):
    if request.method == 'POST':
        skill = request.form.get('skill')
        description = request.form.get('description')
        date = request.form.get('date')

def request_skill(request):
    if request.method == 'POST':
        print('hello')

def bid(request):
    if request.method == 'POST':
        print('bid')