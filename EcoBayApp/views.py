from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def search(request):
    pass

def register(request):
    return render(request, 'register.html')

def login(request):
    pass

def logout(request):
    pass

def categories(request):
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

def get_skill(request):
    pass