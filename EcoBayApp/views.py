from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from .models import Item, Skill, User, Category


def home(request):
    return render(request, 'index.html')

def search(request):

    error = None

    if request.method == 'GET':
        query = request.GET.get('search')
        result = Item.objects.all().filter(name__icontains=query) 
        print(result, 'result')
        if result is None:
            error = f'No results found for {query}'
            return render(request, 'index.html', {
                'error': error
            })
        else:
            return render(request, 'index.html', {
                'items': result
            })

    else:
        return render(request, 'index.html')

def register(request):

    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            error = "Passwords do not match."
            return render(request, "register.html", {"error": error})

        if not all([username, email, password, confirm_password]):
            error = "All fields are required."
            return render(request, "register.html", {"error": error})

        if User.objects.filter(username=username):
            error = 'User already exists'
            return render(request, 'login.html',{
                'error': error
            })
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            return render(request, 'index.html')
    
    return render(request, 'register.html')

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
        categories = Category.objects.all()
        return render(request, 'index.html', {
            'categories': categories
        })
    else:
        return render(request, 'index.html')

def list_items(request):

    if request.method == 'GET':
        items = Item.objects.all()

        return render(request, 'index.html', {
            'items': items
        })
    else:
        return render(request, 'index.html')

def list_items_by_category(request):

    error = None

    if request.method == 'GET':
        category = request.form.get('category')
        items = Item.objects.filter(category)

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

def get_item(request, id):
    item = get_object_or_404(Item, id=id)

    return render(request, 'item.html', {
        'item': item
    })

def get_skill(request, id):

    skill = get_object_or_404(Skill, id=id)

    return render(request, 'skill.html', {
        'skill': skill
    })

def list_skills(request):

    if request.method == 'GET':
        skills = Skill.objects.all()
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
    
def make_offer(request, id):

    error = None

    if request.method == 'POST':
        print('bid')