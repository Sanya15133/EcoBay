from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def search(request):
    pass

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'sign-in.html')

def logout(request):
    pass

def item_categories(request):
    pass

def list_items(request):
    pass

def add_item(request):
    pass

def get_item(request):
    pass

def list_skills(request):
    pass

def add_skill(request):
    pass

def request_skill(request):
    pass

def bid(request):
    pass