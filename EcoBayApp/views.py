from django.shortcuts import render

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
    pass

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
        pass

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
    pass

def bid(request):
    if request.method == 'POST':
        print('bid')