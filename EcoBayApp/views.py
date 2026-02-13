from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import Item, Skill, User, Category


def home(request):

    skills = Skill.objects.all()
    items = Item.objects.all()

    error = None
    if not skills.exists() and not items.exists():
        error = 'No items or skills to be displayed'

    return render(request, 'index.html', {
        'skills': skills,
        'items': items,
        'error': error,
    })

def search(request):

    error = None
    query = request.GET.get('search')

    if not query:
        return render(request, 'index.html')

    if request.method == 'GET':
        items = Item.objects.filter(name__icontains=query)
        skills = Skill.objects.filter(name__icontains=query)
             
        if not items.exists() and not skills.exists():
            error = f'No results found for {query}'
            return render(request, 'index.html', {
                'error': error
            })
        else:
            return render(request, 'index.html', {
                'items': items,
                'skills': skills
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

        if not all([username, email, password, confirm_password]):
            error = "All fields are required."
            return render(request, "register.html", {"error": error})

        if password != confirm_password:
            error = "Passwords do not match."
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

            user = authenticate(username=username, password=password)

            if user:

                login(request, user)
                return redirect('home')
    
    return render(request, 'register.html')

def login_view(request):

    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid username and/or password."
            return render(request, "login.html", {
                "error": error
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('home')

def item_categories(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        
        return render(request, 'add-item.html', {
            'categories': categories
        })

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
    user = request.user
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'add-item.html', {
            'categories': categories
        })

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        amount = request.POST.get('price')
        image_url = request.POST.get('image')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        if not all([name, description, amount, image_url, category]):
            error = 'All fields are required'
            return render(request, "add-item.html", {
                "error": error
            })

        Item.objects.create(name=name, description=description, category=category, amount=amount,
        image_url=image_url, user=user)
        return redirect('home')
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


def add_skill(request):

    error = None
    user = request.user

    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'add-skill.html', {
            'categories': categories
        })

    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        if not all({name, amount, description, category}):
            error = 'All fields required'
            return render(request, 'add-skill.html', {
                'error': error
            })
        else:
            Skill.objects.create(name=name, description=description, amount=amount, category=category, user=user)
            return redirect('home')
    else:
        return render(request, 'add-skill.html')
    
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
            return render(request, 'index.html')
    else:
        return render(request, 'skills-request.html')
    
def make_offer(request, id):
    
    item = get_object_or_404(Item, id=id)
    error = None

    if request.method == 'POST':
        bid_amount = request.POST.get('bid-amount')

        if not bid_amount:
            error = 'Please enter a bid'
        else:
            bid_amount = int(bid_amount)

            if bid_amount <= item.amount:
                error = 'Your bid must be higher than the current bid'
            else:
                item.amount = bid_amount
                item.save()
                return redirect('item', id=item.id)

    return render(request, 'item.html', {
        'item': item,
        'error': error,
    })

    
def delete_item(request, id):
    
    user = request.user
    item = get_object_or_404(Item, id=id)

    if user == item.user:
        item.delete()
        return HttpResponseRedirect(request.path_info)

def delete_skill(request, id):
    
    user = request.user
    skill = get_object_or_404(Skill, id=id)

    if user == skill.user:
        skill.delete()
        return HttpResponseRedirect(request.path_info)





        