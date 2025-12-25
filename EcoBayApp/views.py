from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from .models import Item, Skill, User


def home(request):
    return render(request, 'index.html')

def search(request):

    error = None
    
    if request.method == 'GET':
        query = request.form.get('search')
        result = Item.objects.all().filter(feeder__icontains=query) 
        if result is None:



def register(request):
    print('hello')
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if not all([username, email, password, confirm_password]):
            error = "All fields are required."
            return render(request, "register.html", {"error": error})
        elif password != confirm_password:
            error = "Passwords do not match."
            return render(request, "register.html", {"error": error})
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return redirect(request, "index.html")
    
    return render(request, 'register.html', {'error': error})

def login_view(request):

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            error = "Invalid username and/or password."
            return render(request, "login.html", {
                "error": error
            })
    else:
        return render(request, "login.html")

def logout(request):
    logout(request)
    return redirect('index')

def item_categories(request):

    if request.method == 'GET':
        categories = categories.db.all()



def list_items(request):

    if request.method == 'GET':
        items = Item.db.all()

        return render(request, 'index.html', {
            'items': items
        })
    else:
        return render(request, 'index.html')

def list_items_by_category(request):

    error = None

    if request.method == 'GET':
        category = request.form.get('category')
        items = Item.db.filter(category)

        if items is None:
            error = 'This category has no current items'
            return render(request, 'index.html', {
                'error': error
            })
        else:
            return render(request, 'index.html', {
                'items':items
            })
    else:
        return render(request, 'index.html')


def add_item(request):

    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')

        if not all([name, description, price, image]):
            error = 'All fields are required'
            return render(request, "add-item.html", {
                "error": error
            })

        Item.objects.create(name=name, description=description, price=price, image=image)
        return redirect(request, "index.html")
    
    else:
        return render(request, "add-item.html")

def get_item(request):
    error = None
    if request.method == 'GET':
        query = request.form.get('item')
        item = Item.db.filter(query)
        if not query in item:
            error = f'{query} cannot be found'
            return render(request, 'index.html', {
                'error': error
            })
        else:
            return render(request, 'item.html', {
                'item': item
            })
    else:
        return render(request, 'index.html')

def list_skills(request):
    if request.method == 'GET':
        skills = Skill.db.all()
        return render(request, 'index.html', {
            'skills': skills
        })
    else:
        return render(request, 'index.html')

def add_skill(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('skill')
        description = request.POST.get('description')
        if not all({name, amount, description}):
            error = 'All fields required'
            return render(request, 'add-skill.html', {
                'error': error
            })
        else:
            Skill.objects.create(name=name, description=description, amount=amount)
            return redirect(request, 'index.html')
    else:
        return redirect(request, 'index.html')
    
def request_skill(request):

    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_needed_by = request.POST.get('date')
        is_complete = request.POST.get('is-complete')
        if not all({ name, description, date_needed_by, is_complete}):
            error = 'All fields required'
            return render(request, 'skills-request.html', {
                'error': error
            })
        else:
            Skill.objects.create(name=name, description=description, date_needed_by=date_needed_by, is_complete=is_complete)
            return redirect(request, 'index.html')
    else:
        return redirect(request, 'index.html')
    
def make_offer(request):
    if request.method == 'POST':
        print('bid')